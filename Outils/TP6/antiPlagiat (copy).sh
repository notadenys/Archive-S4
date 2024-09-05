#!/bin/bash

# Le logiciel anti-plagiat

DOSSIER="dossierTPNote"

# on parcour tous les fichiers et l'ajoute dans un liste
FICHIERS=()  #array pour les fichiers
for ETUDIANT in $DOSSIER/*;
do
	for FICHIER in $ETUDIANT/*
	do
		FICHIERS+=($FICHIER)
	done
done

for ((i = 0; i<${#FICHIERS[@]}; i++))
do
	FICHIER1=${FICHIERS[i]}
	name1=$(echo "$FICHIER1" | awk -F '/' '{print $2}')
	content1=$(cat $FICHIER1 | grep -E '[[:alnum:]].*;?')
	variables1=$(echo "$content1" | grep -Ev "(int|float|char)\s\w+\(" | grep -Eo "(int|float|char)\s\w+" )
	functions1=$(echo "$content1" | grep -Eo "(int|float|char|void)\s\w+\(.+\)" )
	for ((j = i; j<${#FICHIERS[@]}; j++))
	do
		FICHIER2=${FICHIERS[j]}
		name2=$(echo "$FICHIER2" | awk -F '/' '{print $2}')
		# si ce sont pas les fichiers de meme eleve
		if [ ! "$name1" == "$name2" ]; then
			content2=$(cat $FICHIER2 | grep -E '[[:alnum:]].*;?')
			variables2=$(echo "$content2" | grep -Ev "(int|float|char)\s\w+\(" | grep -Eo "(int|float|char)\s\w+" )
			functions2=$(echo "$content2" | grep -Eo "(int|float|char|void)\s\w+\(.+\)" )
			
			lignesPlagiat=$(comm -12 <(echo "$content1" | sort) <(echo "$content2" | sort))
			functionsPlagiat=$(comm -12 <(echo "$functions1" | sort) <(echo "$functions2" | sort))
			variablesPlagiat=$(comm -12 <(echo "$variables1" | sort) <(echo "$variables2" | sort))
			echo "$functionsPlagiat"
			echo "$variablesPlagiat"
			echo "$name1 $name2 $lignesPlagiat"
			
		fi
	done
done
