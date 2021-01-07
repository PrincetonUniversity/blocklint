#!/bin/bash

set -e

echo "Config File Tests"
echo "  No config"
if blocklint tests/sample_files/test.* --max-issue-threshold=27 > /dev/null; then
    echo "Failed"
    exit 1
fi

cp tests/.blocklint ./
echo "  Local .blocklint config"
if blocklint tests/sample_files/test.* > /dev/null; then
    echo "Failed"
    rm ./.blocklint
    exit 1
fi

echo "  Local .blocklint config with command line overrides"
blocklint tests/sample_files/test.* --max-issue-threshold=30 > /dev/null || echo "Failed"
rm ./.blocklint

echo " Local setup.cfg config"
cd tests/config_tests/setup
if blocklint ../../sample_files/test.* > /dev/null; then
    echo "Failed"
    exit 1
fi

echo "  Local .setup.cfg config with command line overrides"
blocklint tests/sample_files/test.* --max-issue-threshold=30 > /dev/null || echo "Failed"


echo " Local tox.ini config"
cd ../tox
if blocklint ../../sample_files/test.* > /dev/null; then
    echo "Failed"
    exit 1
fi

echo "  Local .tox.ini config with command line overrides"
blocklint tests/sample_files/test.* --max-issue-threshold=30 > /dev/null || echo "Failed"

echo " Multiple local configs (tox)"
cd ../tox_setup
if blocklint ../../sample_files/test.* > /dev/null; then
    echo "Failed"
    exit 1
fi

echo " Multiple local configs (setup)"
cd ../setup_blocklint
if blocklint ../../sample_files/test.* > /dev/null; then
    echo "Failed"
    exit 1
fi

echo " Flag and list options"
cd ../flag_and_list
diff <(cat ../../sample_files/test.{cc,py,txt} |
        blocklint --stdin ) \
    ../../sample_files/stdin_wordlist.txt

echo Passed!
