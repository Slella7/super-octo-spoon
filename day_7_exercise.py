'''
 
 Exercise : 
        Write a Program to create a list of Continents and 
                                    some of its countries and 
                                    languages spoken in each country 

        Create an empty list and name it "continent_and_countries"
        Create "countries_list" for each continent
        add the countries and languages spoken one by one using append and insert
        Sort the list 
        reverse the list 

'''

continent_and_countries = []

asia_countries_list = ["Asia",
                       ["India", "Hindi", "Telugu"],
                       ["Russia", "Russian"],
                       ["China", "Mandarin"],
                       ["South Korea", "Korean"],
                       ["Japan", "Japanese"]
                       ]

europe_countries_list = ["Europe",
                         ["UK", "English"],
                         ["France", "French"],
                         ["Germany", "German", "English"],
                         ["Ireland", "Irish", "English"],
                         ["Spain", "Spanish"]
                         ]

africa_countries_list = ["Africa",
                         ["Egypt", "Arabic"],
                         ["South Africa", "Zulu", "Afrikaans"],
                         ["Nigeria", "English"],
                         ["Somalia", "Somali", "Arabic"],
                         ["Madagascar", "Malagasy", "French"]
                         ]

south_america_countries_list = ["South America",
                                ["Brazil", "Portuguese"],
                                ["Argentia", "Spanish"],
                                ["Chile", "Spanish"],
                                ["Peru", "Spanish"]
                                ]


continent_and_countries.append(asia_countries_list)

continent_and_countries.append(south_america_countries_list)
print(continent_and_countries)

continent_and_countries.insert(1, europe_countries_list)
print(continent_and_countries)

continent_and_countries.insert(0, africa_countries_list)
print(continent_and_countries)

continent_and_countries.sort()
print(continent_and_countries)

continent_and_countries.reverse()
print(continent_and_countries)
