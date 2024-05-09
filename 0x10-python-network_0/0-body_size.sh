#!/bin/bash

#bash script 
curl -sl "$1" | awk'/Content-Length/ {print $2}'
