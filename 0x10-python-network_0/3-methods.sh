#!/bin/bash
#bash script
curl -sl ALLOW "$1" -L | grep "ALLOW" | cut -d " " -f2-
