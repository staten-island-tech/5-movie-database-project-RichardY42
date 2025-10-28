import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

def genre(type):
    for i in range(len(data)):
        if type in data[i]['genres']:
            print(f"Results:{data[i]['title']} ({data[i]['year']})") 
genre("Action")