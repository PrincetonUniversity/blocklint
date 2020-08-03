import pytest
import re

import blocklint.main as bl


def test_get_args_wordlists(mocker):
    mocker.patch('os.getcwd', return_value='')
    # defaults
    args = bl.get_args()
    assert args == {
        'blocklist': ['blacklist', 'master', 'slave', 'whitelist'],
        'exactlist': [],
        'files': [],
        'wordlist': []}

    # set each list in turn
    args = bl.get_args('--blocklist test'.split())
    assert args == {
        'blocklist': ['test'],
        'exactlist': [],
        'files': [],
        'wordlist': []}

    args = bl.get_args('--exactlist test,test2'.split())
    assert args == {
        'blocklist': [],
        'exactlist': ['test', 'test2'],
        'files': [],
        'wordlist': []}

    args = bl.get_args('--wordlist test2'.split())
    assert args == {
        'blocklist': [],
        'exactlist': [],
        'files': [],
        'wordlist': ['test2']}

    # remove duplicate words
    args = bl.get_args(('--blocklist test,test '
                        '--exactlist test2,test2 '
                        '--wordlist test3,test3').split())
    assert args == {
        'blocklist': ['test'],
        'exactlist': ['test2'],
        'files': [],
        'wordlist': ['test3']}

    # remove words from restrictive lists that are in more permissive ones
    # e.g. blocklist will match words and exact
    args = bl.get_args(('--blocklist test '
                        '--exactlist test '
                        '--wordlist test').split())
    assert args == {
        'blocklist': ['test'],
        'exactlist': [],
        'files': [],
        'wordlist': []}

    args = bl.get_args(('--blocklist test1 '
                        '--exactlist test '
                        '--wordlist test').split())
    assert args == {
        'blocklist': ['test1'],
        'exactlist': [],
        'files': [],
        'wordlist': ['test']}


def test_ignore_special():
    assert '' == bl.ignore_special('')
    assert 'a' == bl.ignore_special('a')
    assert 'a[^a-zA-Z0-9]?b' == bl.ignore_special('ab')
    assert 'a[^a-zA-Z0-9]?b[^a-zA-Z0-9]?c' == bl.ignore_special('abc')


def test_word_boundaries():
    assert '' == bl.word_boundaries('')
    assert r'\ba\b' == bl.word_boundaries('a')
    assert r'\bab\b' == bl.word_boundaries('ab')


def test_generate_re(mocker):
    # to test, just returning the re and if it's ignoring case
    mock_re = mocker.patch('re.compile', side_effect=lambda *x:
                           x[0] + ('i' if len(x) > 1 and x[1] == re.IGNORECASE
                                   else ''))
    assert bl.generate_re({'blocklist': [], 'wordlist': [],
                           'exactlist': []}) == {}

    assert bl.generate_re({'blocklist': ['bab'],
                           'wordlist': ['cac'],
                           'exactlist': ['dad']}) == {
                               'bab': 'b[^a-zA-Z0-9]?a[^a-zA-Z0-9]?bi',
                               'cac': r'\bc[^a-zA-Z0-9]?a[^a-zA-Z0-9]?c\bi',
                               'dad': r'\bdad\b'}


def test_generate_re_matches():
    regexes = bl.generate_re({'blocklist': ['bab', 'longerwordtotest'],
                              'wordlist': ['cac'],
                              'exactlist': ['dad']})

    assert list(bl.check_line('no matches', regexes, 'test', 1)) == []
    assert list(bl.check_line('bab bab bab', regexes, 'test', 1)) == [
        'test:1:1: use of "bab"'  # only match first
    ]
    assert list(bl.check_line('B-a*B bab bab', regexes, 'test', 1)) == [
        'test:1:1: use of "bab"'  # ignore case, special
    ]
    assert list(bl.check_line('this is a l!o@n#g$e%r^w&o*r(d)t-o_t+e=s/t',
                              regexes, 'test', 1)) == [
        'test:1:11: use of "longerwordtotest"'  # special
    ]
    assert list(bl.check_line('more l\\o|n?g[e]r{w}o,r.d<t>o`t~e;s:t',
                              regexes, 'test', 2)) == [
        'test:2:6: use of "longerwordtotest"'  # more special
    ]
    assert list(bl.check_line('hereinababword', regexes, 'test', 3)) == [
        'test:3:8: use of "bab"'  # ignore case, special
    ]

    assert list(bl.check_line('aCAC not found, but !c@A?c. is ',
                              regexes, 'test', 4)) == [
        'test:4:22: use of "cac"'  # ignore case, special
    ]

    assert list(bl.check_line('adad d@ad and DaD are missed, but not ,dad"',
                              regexes, 'test', 5)) == [
        'test:5:40: use of "dad"'  # ignore case, special
    ]
