#!/bin/bash

#svrd [<option>] <nomDossier>
if [ $# -eq 1 ]
then 	
	if [ -d $1 ]
	then 
		cp -r /$1 /$1_SAVE
	else 
		mkdir /$1_SAVE
	fi	
else 
	if [ $# -eq 2 ]
	then
		if [ $1 -eq '-b' ]
		
fi

