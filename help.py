from functools import wraps
import requests
import flask
import sqlite3

def LoginRequired(func):
    @wraps(func)

    def DecoratedFunction(*args, **kwargs):
        if flask.request.args.get("user_id"):
            return func(*args, **kwargs)
        return "You didn't log in"

    return DecoratedFunction


def AddRowToUserTable(sqlConnection, **kwargs):
    possibleKeys = ["name", "password", "favourite_title", "id"]
    for key in kwargs:
        if key not in possibleKeys:
            raise TypeError(key + " is wrong key")

    db = sqlConnection.cursor()
    db.execute(f'INSERT INTO users(name, password, favourite_title, id) VALUES(\"{kwargs["name"]}\", \"{kwargs["password"]}\" , \"{kwargs["favourite_title"]}\", {kwargs["id"]})')
    sqlConnection.commit()
    # for i in kwargs.values():
        
sqlCon = sqlite3.connect("anime.db")
AddRowToUserTable(sqlCon, name="Dima", password="Ya gey", favourite_title="Call me by your name", id=69)
