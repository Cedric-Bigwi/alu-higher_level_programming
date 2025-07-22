#!/bin/bash
# Send a GET request with a custom header to the given URL
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
