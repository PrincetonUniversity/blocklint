#!/bin/bash
set -euo pipefail

echo Acceptance tests
echo "  defaults"
diff <(blocklint tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/default.txt

echo "  blocklist"
diff <(blocklint \
        --blocklist blacklist,whitelist \
        tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/blocklist.txt

echo "  wordlist"
diff <(blocklint \
        --wordlist blacklist \
        tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/wordlist.txt

echo "  exactlist"
diff <(blocklint \
        --exactlist blacklist \
        tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/exactlist.txt

echo "  end position long"
diff <(blocklint \
        --end-pos \
        tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/end.txt

echo "  end position short"
diff <(blocklint \
        -e \
        tests/sample_files/test.{cc,py,txt}) \
    tests/sample_files/end.txt

echo "  stdin"
diff <(cat tests/sample_files/test.{cc,py,txt} |
        blocklint --stdin ) \
    tests/sample_files/stdin.txt

echo "  pragma"
diff <(blocklint tests/sample_files/test_pragma.{cc,py,txt}) \
    tests/sample_files/pragma.txt
echo Passed!
