#!/bin/bash
# Send GET request with custom header and show the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
