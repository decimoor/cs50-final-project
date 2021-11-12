import json

def GetAnimeList(titleName):
    with open("data\\anime.json", encoding='utf-8') as json_file:
        data = json.load(json_file)["data"]
        matches = []
        counter = 0
        for title in data:
            if titleName.lower() in title["title"].lower():
                matches.append(title["title"])
                counter += 1
            if counter > 5:
                break
    return matches

def GetAnimeFullInfo(titleName):
    with open("data\\anime.json", encoding='utf-8') as json_file:
        data = json.load(json_file)["data"]
        matches = []
        counter = 0
        for title in data:
            if titleName in title["title"]:
                return title
        raise("Couldn't find that anime in database")

