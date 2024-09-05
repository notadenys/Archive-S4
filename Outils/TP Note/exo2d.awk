BEGIN {
  	continents = array()
  	countries = array()
}

{
  	split($0, fields, ",")

  	continent = fields[2]
  	country = fields[1]

  	if (!continents[continent]) {
   		continents[continent] = 1
  	}

  	countries[country] = countries[country] ? countries[country] FS continent : continent
}

END {
  	for (country in countries) {
    	if (split(countries[country], conts, FS) > 1) {
      	printf("%s: ", country)
      	for (i in conts) {
        	printf("%s%s", conts[i], (i < split(countries[country], conts, FS) - 1) ? ", " : "")
      	}
      	print("")
    	}
	}
}

