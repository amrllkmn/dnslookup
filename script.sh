#!/bin/bash

read url

text=${url:4:-4}
new=$(echo $text | sed -e 's/\.[a-z]*$//')

./dnslookup ${url} > ${new}.txt

ext=".txt"
file="$new$ext"

echo $file

python ip.py ${file}
