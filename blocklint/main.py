import re
import sys


ignore_class = '[^a-zA-Z0-9]'


# TODO add filename input, default to all files in current dir
def main():
    blocklist = ['master', 'slave', 'whitelist', 'blacklist']
    checkers = [re.compile(condition_re(item), re.IGNORECASE)
                for item in blocklist]

    fname = sys.argv[1]
    with open(fname, 'r') as infile:
        for i, line in enumerate(infile, 1):
            for c, name in zip(checkers, blocklist):
                match = c.search(line)
                if match:
                    print(f'{fname}:{i}:{match.start()+1}: use of "{name}"')


def condition_re(input_pattern):
    return (ignore_class + '?').join(list(input_pattern))


if __name__ == '__main__':
    main()
