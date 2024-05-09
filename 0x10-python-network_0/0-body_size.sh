#!/bin/bash

if [ $# -ne 1 ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

URL=$1

BODY_SIZE=$(curl -sI $URL | grep -i "content-length" | awk '{print $2}' | tr -d '\r')

if [ -z "$BODY_SIZE" ]; then
	    BODY_SIZE=$(curl -s $URL | wc -c)
fi

echo $BODY_SIZE
