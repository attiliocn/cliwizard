#!/bin/bash

# Get the path of the script's directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Source each function file
source "$SCRIPT_DIR/functions.sh"
