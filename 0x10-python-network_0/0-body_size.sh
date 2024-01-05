#!/bin/bash
# A script that send reauest and retrieves the byte size of the HTTP response header for a given URL
curl -s "$1" | wc -c
