#!/bin/bash
# Display size of body of response; ./0-body_size.sh <url>
curl -s "$1" | wc -c
