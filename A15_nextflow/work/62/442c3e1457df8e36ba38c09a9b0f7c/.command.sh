#!/bin/bash -ue
echo "[inputString:Hello World]" | tr '[:lower:]' '[:upper:]' > output.txt
