#!/bin/bash
#bash script 
curl -sl "$1" | grep"Content-Length" | cut -d " " -f2
