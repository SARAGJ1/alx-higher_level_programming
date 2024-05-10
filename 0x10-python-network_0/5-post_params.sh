#!/bin/bash
# bash script
curl -sX POST $1 -d "email=test@gmail.com&subject=l will always be here for PLD" -L
