import sys


def main(blacklist, white_list):
    # looking for master slave
    for item in blacklist:
        if item in white_list:
            slave = item


if __name__ == '__main__':
    main()
