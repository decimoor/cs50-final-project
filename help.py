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