#!/bin/bash
# Display body size of the response
curl -s "$1" | wc -c
