mother_rivers = {
    'nile': 'egypt',
    'yellowriver': 'china',
    'amazon': 'brazil',
    'danube': 'U.K.',
    'ganges': 'india'
}
for river, country in mother_rivers.items():
    print("The {} runs through {}".format(river, country))
print()
for river in mother_rivers.keys():
    print(river)
print()
for country in mother_rivers.values():
    print(country)
