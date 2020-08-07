# blocklint

If you've used a modern IDE, you know the importance of immediate feedback
for compilation errors or even stylistic slip ups.  Knowing all variables
should be declared or that lines must be less than 80 characters long is good,
but adhering to those rules takes a back seat when in the flow of writing
code.  A linter brings these issues back into your consciousness by
highlighting the problematic lines of code.  Over time, the enforced style
becomes more intuitive but the linter is always there to nudge you if you slip.

We are in the midst of changing attitudes towards words and phrases that are
not inclusive. Not only are developers acknowledging the offensive history of
terms like "master/slave" and "blacklist/whitelist", but we are taking active
steps to remove their usage and replace them with more appropriate language. 
This tool is not a commentary on inclusion, but rather a utility to detect
whatever words you'd like to remove from code.

[Alex.js](alexjs.com) is one option for highlighting offensive language,
but it is geared towards text documents such as markdown, misses common
constructs in source code and is also overly broad and prone to false
positives.  Blocklint is built with source code in mind and is more limited
in scope.

## Requirements and Installation
Blocklint is written in python and uses minimal, standard libraries.  It has
been tested for python >= 2.7  To install:

```
pip install git+https://github.com/troycomi/blocklint
```
into an appropriate environment.

## Usage
Without any arguments, blocklint will search all files in the current directory
for uses of master, slave, blacklist and whitelist:
```bash
$ pwd
/path/to/blocklint/blocklint
$ blocklint
/path/to/blocklint/blocklint/main.py:40:60: use of "blacklist"
/path/to/blocklint/blocklint/main.py:40:37: use of "master"
/path/to/blocklint/blocklint/main.py:40:44: use of "slave"
/path/to/blocklint/blocklint/main.py:40:50: use of "whitelist"
/path/to/blocklint/blocklint/main.py:55:53: use of "blacklist"
/path/to/blocklint/blocklint/main.py:55:30: use of "master"
/path/to/blocklint/blocklint/main.py:55:37: use of "slave"
/path/to/blocklint/blocklint/main.py:55:43: use of "whitelist"
```

Optionally, multiple files and directories can be specified to search.  The
detected words can be customized through several options; setting any will
clear the defaults.  Multiple words are specified as comma separated values:
 - blocklist: Will match any occurrence of the word, ignoring case and special
   characters.
 - wordlist: Will match the word, ignoring case and special characters but
   respecting word boundaries.
 - exactlist: Will match the word as entered respecting word boundaries.

Only the first match of a word in a line will be returned, but multiple words
can match on a single line.  Here are some examples:
```bash
$ blocklint --blocklist test,asdf <(echo thisTEST will match as will a_S-d:F)
/dev/fd/63:1:29: use of "asdf"
/dev/fd/63:1:5: use of "test"

$ blocklint --wordlist test,asdf <(echo thisTEST will not match but T=E-ST, will)
/dev/fd/63:1:29: use of "test"

$ blocklint --exactlist Test <(echo thisTest, tEST, T-est fail but Test! matches)
/dev/fd/63:1:32: use of "Test"
```
The `-e,--end-pos` flag will provide the end position of the match in addition
to the start position.

The `--stdin` flag will take values from stdin instead of a file or directory.

## Integration with ALE
Blocklist can be used with [ALE](https://github.com/dense-analysis/ale) for
vim by adding the following to your vimrc:
```vim
" Inclusive syntax {{{1
augroup BlocklintALE
  autocmd!
  autocmd User ALEWantResults call BlocklintHook(g:ale_want_results_buffer)
augroup END

function! BlocklintHook(buffer) abort
  " Tell ALE we're going to check this buffer.
  call ale#other_source#StartChecking(a:buffer, 'blocklint')
  call ale#command#Run(a:buffer, 'blocklint -e --stdin',
              \ function('BlocklintWorkDone'), {'read_buffer': 1})
endfunction

function! BlocklintWorkDone(buffer, results, metadata) abort
  " Send results to ALE after they have been collected.
  let l:pattern = '\v^[^:]+:(\d+):(\d+):(\d+): (.+)$'
  let l:output = []
  for l:match in ale#util#GetMatches(a:results, l:pattern)
    call add(l:output, {
              \ 'lnum': l:match[1],
              \ 'col': l:match[2],
              \ 'end_col': l:match[3],
              \ 'text': l:match[4],
              \ 'type': 'E'})
  endfor
  call ale#other_source#ShowResults(a:buffer, 'blocklint', l:output)
endfunction
```
