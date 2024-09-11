#!/bin/bash

for f in $@; do cat -v "$f" | sed 's/M-BM-//g' > tmp && cp "$f" "$f".bak && mv tmp "$f"; done