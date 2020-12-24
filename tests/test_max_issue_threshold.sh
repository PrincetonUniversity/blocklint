#!/bin/bash

set -e

echo "Max threshold tests"
echo "  No threshold"
blocklint tests/sample_files/test.* > /dev/null  || echo "Failed"

echo "  Issue count under threshold"
blocklint tests/sample_files/test.* --max-issue-threshold=100 > /dev/null  \
    || echo "Failed"

echo "  Issue count one over threshold"
blocklint tests/sample_files/test.* --max-issue-threshold=28 > /dev/null  \
    || echo "Failed"

echo "  Issue count at threshold"
if blocklint tests/sample_files/test.* --max-issue-threshold=27 > /dev/null; then
    echo "Failed"
    exit 1
fi

echo "  Issue count under threshold"
if blocklint tests/sample_files/test.* --max-issue-threshold=26 > /dev/null; then
    echo "Failed"
    exit 1
fi

echo Passed!
