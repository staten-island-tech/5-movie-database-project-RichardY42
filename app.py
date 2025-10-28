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
        print(data[i]['title']) 

limitbottom=input("give me a year I will print all movies that released after that year: ")
limittop=input("give me a another year i'll print all the moives before it: ")
for i in range(len(data)):
    if data[i]['year'] > int(limitbottom) and data[i]['year'] < int(limittop):
        print(data[i]['title'])

year=input("give me a year I will print all movies that released during that year: ")
for i in range(len(data)):
    if data[i]['year'] == int(year):
        print(data[i]['title']) 
movname=input("Search movie title: ")
for i in range(len(data)):
    if data[i]['title'] == movname:
        print(f"Results:{data[i]['title']} ({data[i]['year']})")
    
def Search(movname):
    for i in range(len(data)):
        if data[i]['title'] == movname:
            print(f"Results:{data[i]['title']} ({data[i]['year']})") 
Search("Spider-Man") """

def genre(type):
    for i in range(len(data)):
        if type in data[i]['genres']:
            print(f"Results:{data[i]['title']} ({data[i]['year']})") 
genre('Action')




