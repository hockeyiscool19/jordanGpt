#!/bin/bash

# Default flags
build=false
run=false

# Parse command-line options
while getopts "br" OPTION; do
    case $OPTION in
    b)
        build=true
        ;;
    r)
        run=true
        ;;
    *)
        echo "Usage: $0 [-b (build) -r (run)]"
        exit 1
        ;;
    esac
done

# Perform the desired operations
if $build; then
    echo "Building Docker image..."
    docker build -t jordangpt .
fi

if $run; then
    echo "Running Docker container..."
    docker run -p 7860:7860 jordangpt
fi

# If no options are provided, show usage
if [ "$OPTIND" -eq 1 ]; then
    echo "Usage: $0 [-b (build) -r (run)]"
fi
