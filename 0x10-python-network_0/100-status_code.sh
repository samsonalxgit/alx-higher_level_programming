#!/bin/bash
# bash script to display status code of server
curl -s -o /dev/null -w "%{http_code}" "$1"
