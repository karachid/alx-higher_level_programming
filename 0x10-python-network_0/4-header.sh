#!/bin/bash
# A script that sends a GET request to a given URL with a header variable
curl -sH "X-School-User-Id: 98" "$1"
