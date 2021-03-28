# Obtain data karora
Commands to retrieve data from karora and copy the datasets to the local system:
For the dependent variable snert in for December 2015. The same command is used for January 2016, December 2016, January 2017, December 2017 and January 2018, with the dates changed. Combining all the matched tweets in all months for variable snert becomes snert.txt

zless /net/corpora/twitter2/Tweets/2015/12/201512*.out.gz | /net/corpora/twitter2/tools/tweet2tab user.location text | grep -wi 'snert'  | grep -vi ‘erwtensoep’ > ~/IWO_project/snert_2015_12.txt 

For the dependent variable erwtensoep in for December 2015. The same command is used for January 2016, December 2016, January 2017, December 2017 and January 2018, with the dates changed. Combining all the matched tweets in all months for variable erwtensoep becomes erwtensoep.txt

zless /net/corpora/twitter2/Tweets/2015/12/201512*.out.gz | /net/corpora/twitter2/tools/tweet2tab user.location text | grep -wi 'erwtensoep'  | grep -vi ‘snert’ > ~/IWO_project/erwtensoep_2015_12.txt 

# Independent variables north and south
Lists copied from Wikipedia and combined to make a list for all the places in the northern region. Combining them becomes north.txt

Link to places in Friesland: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_Friesland

Link to places in Groningen: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_Groningen

Link to places in Drenthe: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_Drenthe 

Lists copied from Wikipedia and combined to make a list for all the places in the southern region. Combining them becomes south.txt

Link to places in Zeeland: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_Zeeland

Link to places in Noord-Brabant: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_North_Brabant

Link to places in Limburg: https://en.wikipedia.org/wiki/List_of_cities,_towns_and_villages_in_Limburg_(Netherlands)

# List double places
List copied from Wikipedia containing double places in the Netherlands:
https://nl.wikipedia.org/wiki/Lijst_van_gelijkluidende_Nederlandstalige_plaatsnamen

# Command line for Python script pre-processing double places
python3 double_places.py copy_wiki_double.txt > double_places_nl.txt

# Command line Bash script and Python script for final project
./project.sh erwtensoep.txt snert.txt
