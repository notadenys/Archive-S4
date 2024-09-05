#!/bin/bash

# Le logiciel anti-plagiat

DOSSIER="dossierTPNote"

# on parcourt tous les fichiers et les ajoute dans une liste
FICHIERS=()  # tableau pour les fichiers
for ETUDIANT in $DOSSIER/*;
do
    for FICHIER in $ETUDIANT/*
    do
        FICHIERS+=("$FICHIER")
    done
done

for ((i = 0; i<${#FICHIERS[@]}; i++))
do
    FICHIER1="${FICHIERS[i]}"
    name1=$(echo "$FICHIER1" | awk -F '/' '{print $2}')
    content1=$(cat "$FICHIER1" | grep -Eo '[[:alnum:]].*;?')
    variables1=$(echo "$content1" | grep -Ev "(int|float|char)\s\w+\(" | grep -Eo "(int|float|char)\s\w+" )
    functions1=$(echo "$content1" | grep -Eo "(int|float|char|void)\s\w+\(.+\)" )
    for ((j = i+1; j<${#FICHIERS[@]}; j++))
    do
        FICHIER2="${FICHIERS[j]}"
        name2=$(echo "$FICHIER2" | awk -F '/' '{print $2}')
        # si ce ne sont pas les fichiers du même élève
        if [ ! "$name1" == "$name2" ]; then
            content2=$(cat "$FICHIER2" | grep -Eo '[[:alnum:]].*;?')
            variables2=$(echo "$content2" | grep -Ev "(int|float|char)\s\w+\(" | grep -Eo "(int|float|char)\s\w+" )
            functions2=$(echo "$content2" | grep -Eo "(int|float|char|void)\s\w+\(.+\)" )
            
            nbLignesPlagiat=$(comm -12 <(echo "$content1" | sort) <(echo "$content2" | sort) | wc -l)
            nbFunctionsPlagiat=$(comm -12 <(echo "$functions1" | sort) <(echo "$functions2" | sort) | wc -l)
            nbVariablesPlagiat=$(comm -12 <(echo "$variables1" | sort) <(echo "$variables2" | sort) | wc -l)
            echo "$(comm -12 <(echo "$variables1" | sort) <(echo "$variables2" | sort))"
            echo "$variables1 nigga"
            echo "$variables2"
            
            nbLignes=$(echo "$content1" | wc -l)
            nbFonctions=$(echo "$functions1" | wc -l)
            nbVariables=$(echo "$variables1" | wc -l)
            
            if (( $(echo "$nbLignesPlagiat/$nbLignes > 0.6" | bc -l) )); then
                lignesPlagiat="Oui"
            else
                lignesPlagiat="Non"
            fi
            
            if (( $(echo "$nbFunctionsPlagiat/$nbFonctions > 0.6" | bc -l) )); then
                fonctionsPlagiat="Oui"
            else
                fonctionsPlagiat="Non"
            fi
            
            if (( $(echo "$nbVariablesPlagiat/$nbVariables > 0.6" | bc -l) )); then
                variablesPlagiat="Oui"
            else
                variablesPlagiat="Non"
            fi
            
            echo -e "$name1 $name2 \nLignes plagiat : $nbLignesPlagiat/$nbLignes Plagiat : $lignesPlagiat\nFonctions plagiat : $nbFunctionsPlagiat/$nbFonctions Plagiat : $fonctionsPlagiat\nVariables plagiat : $nbVariablesPlagiat/$nbVariables Plagiat : $variablesPlagiat"
        fi
    done
done

