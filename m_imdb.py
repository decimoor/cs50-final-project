import json
import help

def GetAnimeList(titleName):
    matches = []
    iter = 0
    for titleName in help.GetTitlesLike(str(titleName)):
        matches.append(titleName[1])
        iter += 1
        if iter > 6:
            break
    return matches

def GetAnimeFullInfo(titleName):
    # with open("data\\anime.json", encoding='utf-8') as json_file:
    #     data = json.load(json_file)["data"]
    #     matches = []
    #     counter = 0
    #     for title in data:
    #         if titleName in title["title"]:
    #             return title
    #     raise("Couldn't find that anime in database")
    raise("Couldn't find that anime in database")

