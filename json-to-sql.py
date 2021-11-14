from os import error
import flask
import sqlite3
import help
import json

# from json file we need next values:
# title
# picture
# tags

def ShowJSON():
    with open("data\\anime.json", encoding='utf-8') as json_file:
        data = json.load(json_file)["data"]
        iter = 0
        for info in data:
            title = {
                "title" : info["title"],
                "picture" : info["picture"],
                "tags" : info["tags"]
            }
            iter += 1
            print(title)
            if iter > 10:
                break

def ConvertJSONtoSQLdb():
    with open("data\\anime.json", encoding='utf-8') as json_file:
        data = json.load(json_file)["data"]
        iter = 0
        for info in data:
            iter += 1
            info["title"] = info["title"].replace("\"", "&)")
            try:
                tags = " ".join(str(item) for item in info["tags"])
                help.AddRowToTitlesTable(title_name = info["title"], picture = info["picture"], tags = tags)
            except:
                print("Error!!! "  "Title: " + info["title"], "Picture: " + info["picture"], "Info: ", *info["tags"])
                print(error)
            else:
                print("Title: " + info["title"], "Picture: " + info["picture"], "Info: ", *info["tags"])
        

ConvertJSONtoSQLdb()