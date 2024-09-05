BEGIN{ nb = 0; printf("Ma liste est la suivante :\n") }
{ printf("* %d %s (%ss) ;\n", $3, $2, $1); nb += $3 }
END{ printf("Soit %d produits.\n", nb) }
