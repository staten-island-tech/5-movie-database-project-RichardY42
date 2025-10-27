import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for i in range(len(data)):
    print(data[i]['year'])

year=input("give me a year I will print all movies that released after that year: ")
for i in range(len(data)):
    if data[i]['year'] > int(year):
        print(data[i]['title']) """

afteryear=input("give me a year I will print all movies that released after that year: ")
beforeyear=input("give me a another year i'll print all the moives before it: ")
for i in range(len(data)):
    if data[i]['year'] > int(afteryear):
        print(data[i]['title'])
    if data[i]['year'] < int(afteryear):
            print(data[i]['title'])
