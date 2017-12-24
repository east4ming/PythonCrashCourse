favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pytoon',
}

survey_people = ( 'jen', 'sarah', 'casey', 'eve')
for person in survey_people:
    if person in favorite_languages.keys():
        print("Thank you for join the survey: {}".format(person))
    else:
        print("{}, can you spent a little time to take the survey?".format(person))
