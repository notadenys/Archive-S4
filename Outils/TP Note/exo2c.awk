BEGIN{print "# BEGIN #"; OFS = ","}
{
	if ( $1 == "Continent" ) 
	{
		printf("%s,Diff de population\n",$0);
	} 
	else 
	{
		printf("%s,%d\n",$0,$6-$4)}
	} 
END{print "# END #"}
