#!/bin/bash

#stat exo1.sh | awk '{if ($1=="Access:" && $3!="Uid:"){ split($2,a,"-"); split($3,b,":"); printf("Fichier accédé le %s/%s/%d à %sH %sMin et %dS.\n", a[3], a[2], a[1]%2000, b[1], b[2], b[3]);}}'

for FILE in *;
do
	if [[ -d $FILE ]]
	then
		type="Dossier"
	else
		type="Fichier"
	fi
	stat $FILE | awk '{if ($1=="Access:" && $3!="Uid:"){ split($2,a,"-"); split($3,b,":"); printf("'"$type"' '"$FILE"' accédé le %s/%s/%d à %sH %sMin et %dS ", a[3], a[2], a[1]%2000, b[1], b[2], b[3]); } if ($1=="Modify:"){ split($2,a,"-"); split($3,b,":"); printf("et modifié le %s/%s/%d à %sH %sMin et %dS.\n", a[3], a[2], a[1]%2000, b[1], b[2], b[3]); }}'
done
