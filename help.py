from functools import wraps
import requests
import flask
import sqlite3


# Title's layout
# [0] - id
# [1] - picture's url
# [2] - tags


def LoginRequired(func):
    @wraps(func)

    def DecoratedFunction(*args, **kwargs):
        if flask.request.args.get("user_id"):
            return func(*args, **kwargs)
        return flask.render_template("register.html", errmsg="No errors")

    return DecoratedFunction


def GetWatchedTitles(userID):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    titles = db.execute(f'SELECT * FROM watched_titles WHERE owners_id = {userID}').fetchall()
    sqlconnection.commit()
    titlesDicts = []
    for title in titles:
        titleElement = db.execute(f'SELECT * FROM titles WHERE id = {title[1]}').fetchall()[0]
        sqlconnection.commit()
        titleDict = {
            "titleName": titleElement[1],
            "description": title[3],
            "rating": title[2],
            "img": titleElement[2],
            "tags": titleElement[3]
        }
        titlesDicts.append(titleDict)


    # function returns a list where every element represents next dictionary
    # titleName
    # description
    # rating
    # img
    # tags

    return titlesDicts

def GetUnwatchedTitles(userID):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    titles = db.execute(f'SELECT * FROM unwatched_titles WHERE owners_id = {userID}').fetchall()
    sqlconnection.commit()
    titlesDicts = []
    for title in titles:
        titleElement = db.execute(f'SELECT * FROM titles WHERE id = {title[1]}').fetchall()[0]
        sqlconnection.commit()
        titleDict = {
            "titleName": titleElement[1],
            "img": titleElement[2],
            "tags": titleElement[3]
        }
        titlesDicts.append(titleDict)


    # function returns a list where every element represents next dictionary
    # titleName
    # img
    # tags

    return titlesDicts


def GetTitle(titleName):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    title = db.execute(f'SELECT * FROM titles WHERE title_name LIKE \'{titleName}%\'').fetchall()
    # check if it could find anything
    if len(title) == 0:
        print("Couldn't find anything")
    sqlconnection.commit()
    # we return only 0 becouse there is only one element
    return title[0]

def AddRowToTitlesTable(**kwargs):
    """
    title_name, picture, tags
    """
    possibleKeys = ["title_name", "picture", "tags"]
    for key in kwargs:
        if key not in possibleKeys:
            raise TypeError(key + " is wrong key")
    sqlConnection = sqlite3.Connection("anime.db")
    db = sqlConnection.cursor()
    db.execute(f'INSERT INTO titles(title_name, picture, tags) VALUES(\"{kwargs["title_name"]}\", \"{kwargs["picture"]}\", \"{kwargs["tags"]}\")')
    sqlConnection.commit()

def AddRowToUserTable(**kwargs):
    possibleKeys = ["name", "password", "favourite_title", "id"]
    for key in kwargs:
        if key not in possibleKeys:
            raise TypeError(key + " is wrong key")
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    db.execute(f'INSERT INTO users(name, password, favourite_title) VALUES(\"{kwargs["name"]}\", \"{kwargs["password"]}\" , \"{kwargs["favourite_title"]}\")')
    sqlconnection.commit()

def CheckExisting(name):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    names = db.execute(f'SELECT name FROM users').fetchall()

    for iter in names:
        if name in iter[0]:
            return True
    
    sqlconnection.commit()
    return False

def GetTitlesLike(titleName):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    names = db.execute(f'SELECT * FROM titles WHERE title_name LIKE \'{titleName}%\' ').fetchall() 
    sqlconnection.commit()
    return names

def GetUserId(userName):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    names = db.execute(f'SELECT id FROM users WHERE name = \'{userName}\' ').fetchall() 
    sqlconnection.commit()
    return int(names[0][0])


def AddToWatchedTitles(title):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    # !!!this is release function !!!
    # db.execute(f'INSERT INTO watched_titles (owners_id, title_id, rating, description) VALUES({flask.session["id"]}, {title["id"]}, {title["rating"]}, {title["description"]}')
    # !!! this is debug function !!!
    db.execute(f'INSERT INTO watched_titles (owners_id, title_id, rating, description) VALUES(4, {title["id"]}, {title["rating"]}, \'{title["description"]}\')')
    sqlconnection.commit()

def AddToUnwatchedTitles(title, userId):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    # !!! this is debug function !!!
    db.execute(f'INSERT INTO unwatched_titles (owners_id, title_id) VALUES(4, {title["id"]})')
    # proper version of function looks like this 
    # db.execute(f'INSERT INTO watched_titles (owners_id, title_id) VALUES(userId, {title["id"]})')
    sqlconnection.commit()


tmp = {
    "id": 51
}

AddToUnwatchedTitles(tmp, 1)