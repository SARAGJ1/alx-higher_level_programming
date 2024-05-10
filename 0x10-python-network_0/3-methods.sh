#!/bin/bash
#bash script
curl -si "$1" | awk -F "'/Allo</ {print $2}'
