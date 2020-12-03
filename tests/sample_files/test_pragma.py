def main(blacklist, white_list):  # blocklint: pragma
    # looking for master slave blocklint: pragma
    for item in blacklist:  # blocklint: some other tags pragma
        if item in white_list:  # blocklint: pragma
            slave = item  # blocklint: pragma
            assert slave == item


if __name__ == '__main__':
    main("", "")
