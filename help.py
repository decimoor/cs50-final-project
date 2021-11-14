from functools import wraps
import requests
import flask
import sqlite3



def LoginRequired(func):
    @wraps(func)

    def DecoratedFunction(*args, **kwargs):
        if flask.request.args.get("user_id"):
            return func(*args, **kwargs)
        return flask.render_template("register.html", errmsg="No errors")

    return DecoratedFunction


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
    # for i in kwargs.values():

def CheckExisting(name):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    names = db.execute(f'SELECT name FROM users').fetchall()

    for iter in names:
        if name in iter[0]:
            return True
    
    sqlconnection.commit()
    return False

# AddRowToUserTable(name = "Olzhas", password = "altaireiloveu", favourite_title = "Boku no Piko")
def GetTitlesLike(titleName):
    sqlconnection = sqlite3.Connection("anime.db")
    db = sqlconnection.cursor()
    names = db.execute(f'SELECT * FROM titles WHERE title_name LIKE \'{titleName}%\' ').fetchall() 
    sqlconnection.commit()
    return names
