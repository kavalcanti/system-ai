#!/bin/bash

# Define the alias you want to add
ALIAS_NAME="sys-ai"
ALIAS_COMMAND="$(cd "$(dirname "$0")" && pwd)/sys-ai"

# Check if the alias already exists in the ~/.bashrc file
if grep -q "alias $ALIAS_NAME=" ~/.bashrc; then
    echo "Error: Alias '$ALIAS_NAME' already exists in ~/.bashrc"
    exit 1
fi

# Add the alias to the end of the ~/.bashrc file
echo "alias $ALIAS_NAME='$ALIAS_COMMAND'" >> ~/.bashrc

# Reload the ~/.bashrc file to make the alias available in the current shell
source ~/.bashrc

# Print a success message
echo "Success: Alias '$ALIAS_NAME' has been added to ~/.bashrc"
