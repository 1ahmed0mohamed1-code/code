#!/bin/bash

set -e

git add .

if ! git diff --cached --quiet; then
    git commit -m "Update Python code"
    git push
else
    echo "No changes to upload."
fi
