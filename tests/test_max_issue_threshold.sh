#!/bin/bash

set -e

echo "No threashold..."
blocklint sample_files/test.* > /dev/null

echo "Issue count under threashold..."
blocklint sample_files/test.* --max-issue-threashold=100 > /dev/null

echo "Issue count one over threashold"
blocklint sample_files/test.* --max-issue-threashold=28 > /dev/null

echo "Issue count at threashold"
if blocklint sample_files/test.* --max-issue-threashold=27 > /dev/null; then
    exit 1
fi

echo "Issue count under threashold"
if blocklint sample_files/test.* --max-issue-threashold=20 > /dev/null; then
    exit 1
fi

echo "Done"
