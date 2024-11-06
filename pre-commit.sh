#!/bin/bash

# Paths are relative to the root of the git repository
black .

# add this file to .git/hooks/pre-commit
# touch .git/hooks/pre-commit
# chmod +x .git/hooks/pre-commit
# copy contents of this file