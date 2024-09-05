#!/bin/bash

# Définir les variables
fichier_cpuinfo="/proc/cpuinfo"
fichier_meminfo="/proc/meminfo"

# Fonction pour afficher les informations de la mémoire
function afficher_memoire() {
  taille_adresse_virtuelle=$(awk '{if ($1 == "address") print $4}' "$fichier_cpuinfo" | head -1)
  taille_adresse_physique=$(awk '{if ($1 == "address") print $7}' "$fichier_cpuinfo" | head -1)

  echo "Taille d'une adresse virtuelle: ${taille_adresse_virtuelle} octets"
  echo "Taille d'une adresse physique: $taille_adresse_physique octets"

  echo ""

  taille_memoire_totale=$(awk '{if ($1 == "MemTotal:") print $2}' "$fichier_meminfo")
  taille_memoire_libre=$(awk '{if ($1 == "MemFree:") print $2}' "$fichier_meminfo")
  taille_tables_pages=$(awk '{if ($1 == "PageTables:") print $2}' "$fichier_meminfo")

  echo "Taille totale de la mémoire: $taille_memoire_totale Ko"
  echo "Taille de la mémoire libre: $taille_memoire_libre Ko"
  echo "Taille des tables de pages: $taille_tables_pages Ko"
  
  echo ""
  
  info=$(ps aux | grep "notaden+")
  memoire_utilise=$(echo "$info" | awk '{sum+=$6} END {print sum}')
  pids=$(echo "$info" | awk '{print $2}')
  echo "Taille de mémoire utilisée: $memoire_utilise"
  
  for pid in $pids
  do
  	echo "Process : $pid"
  	if [ -d /proc/$pid ]; then
	  	echo "Max stack size : $(awk '{if ($2 == "stack") print $4}' "/proc/$pid/limits")"
	  	echo "Taille de la mémoire virtuelle utilisée : $(awk '{if ($1 == "VmSize:") print $2}' "/proc/$pid/status")"
	  	echo "Taille de la pile utilisateur : $(awk '{if ($1 == "VmStk:") print $2}' "/proc/$pid/status")"
	  	echo "Taille des données : $(awk '{if ($1 == "VmData:") print $2}' "/proc/$pid/status")"
	  	echo "Taille du texte : $(awk '{if ($1 == "VmExe:") print $2}' "/proc/$pid/status")"
	  	echo "Taille de la table de pages : $(awk '{if ($1 == "VmPTE:") print $2}' "/proc/$pid/status")"
	  else echo "Directory doesn't exist"
	  fi
  	echo ""
  done
  
  pourcentage_mem=$(echo "scale=2; 100*$memoire_utilise"/"$taille_memoire_totale" | bc)
  echo "Pourcentage de mémoire utilisée: $pourcentage_mem%"
}

# Appeler la fonction
afficher_memoire
