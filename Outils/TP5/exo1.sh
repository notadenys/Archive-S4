#!/bin/bash

URL="https://members.loria.fr/MDuflot/files/publis.html"

content=$(curl -s "$URL") 

echo "$content" | grep -E 'http[s]?' | grep -Eo '["http"][s]?.*[.](pdf|PDF)' | awk -F '"' '{print $2}' > listePdf.txt
