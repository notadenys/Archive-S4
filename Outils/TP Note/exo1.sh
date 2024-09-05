#!/bin/bash

# partie HTML
contentHTML=$(cat $1)

classesHTML=$(echo "$contentHTML" | grep -Eo "class=.*\"" | sort | uniq | awk -F '"' '{print $2}')
idsHTML=$(echo "$contentHTML" | grep -Eo "id=.*\"" | sort | uniq | awk -F '"' '{print $2}')

# partie CSS
fichiersCSS=$(echo "$contentHTML" | grep -Eo "link.*" | grep -Eo "[[:alnum:]]*\.css")

contentCSS=''
while IFS= read -r line; do
	contentCSS+=$(cat "$line")
	contentCSS+=' '
done <<< "$fichiersCSS"

classesCSS=$(echo "$contentCSS" | grep -Eo "\.[a-Z]+" | grep -Eo '[a-Z]+' | sort | uniq)
idsCSS=$(echo "$contentCSS" | grep -Eo "\#[a-Z]+" | grep -Eo '[a-Z]+' | sort | uniq)

# partie resultat
echo "Classes absents dans CSS : "
comm -23 <(echo "$classesHTML" | tr ' ' '\n' | sort) <(echo "$classesCSS" | tr ' ' '\n' | sort)
echo ''
echo "IDs absents dans CSS : "
comm -23 <(echo "$idsHTML" | tr ' ' '\n' | sort) <(echo "$idsCSS" | tr ' ' '\n' | sort)
