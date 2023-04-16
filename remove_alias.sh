#!/bin/bash

# Define the alias you want to remove
ALIAS_NAME="sys-ai"

# Check if the alias exists in the ~/.bashrc file
if ! grep -q "alias $ALIAS_NAME=" ~/.bashrc; then
    echo "Error: Alias '$ALIAS_NAME' does not exist in ~/.bashrc"
    exit 1
fi

# Remove the alias from the ~/.bashrc file
sed -i "/alias $ALIAS_NAME=/d" ~/.bashrc

# Reload the ~/.bashrc file to remove the alias from the current shell
source ~/.bashrc

# Print a success message
echo "Success: Alias '$ALIAS_NAME' has been removed from ~/.bashrc"

