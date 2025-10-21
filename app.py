import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

"""for i in range(len(data)):
    print(data[i]['year'])

year=input("give me a year I will print all movies after that year: ")
for i in range(len(data)):
    if int(data['year']) > int(year):
        print(data['year'])"""
print(data['year'])