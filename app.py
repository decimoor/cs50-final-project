import flask
import help
import sqlite3
import m_imdb
import json

sqliteConnection = sqlite3.connect("anime.db")

app = flask.Flask(__name__)

@app.route("/")
@help.LoginRequired
def main():
    if flask.request.form.get("LogOut"):
        return "You have logged out"
        # logs out user from web app
    if flask.request.form.get("AddTitle"):
        return "Add Title menu"
        # redirects to add title route
    if flask.request.form.get("Logo"):
        return "Hello, mate!"
        # reloads page
    # returns main web page if not argiments were passed
    return "Hello, mate!"   


# get anime list function
@app.route("/getAnimeList", methods=["GET", "POST"])
def getAnimeList():
    titleName = flask.request.args.get("titleName")
    matchesTitles = m_imdb.GetAnimeList(titleName)
    return json.dumps(matchesTitles)

@app.route("/register", methods=["GET", "POST"])
def register():
    # this route might get errmsg val which contains error message
    # if there is such a value function sends it to template, so user will see that
    errmsg = "No errors"
    if flask.request.args.get("errmsg"):
        errmsg = flask.request.args.get("errmsg")

    # just return register html file via flask.render_template function
    return flask.render_template("register.html", errmsg = errmsg)

@app.route("/registered", methods=["GET", "POST"])
def registered():
    # checking user input
    # check if user didn't write any info
    if not flask.request.form.get("username") and not flask.request.form.get("password") and not flask.request.form.get("confirmation"):
        return flask.redirect("/register?errmsg=You didn't write any info!!!")

    # check if user didn't write username/password/confirmation 
    if not flask.request.form.get("username"):
        return flask.redirect("/register?errmsg=You didn't write your username")
    if not flask.request.form.get("password"):
        return flask.redirect("/register?errmsg=You didn't write your password")
    if not flask.request.form.get("password-confirmation"):
        return flask.redirect("/register?errmsg=You didn't confirm your password")
    if not flask.request.form.get("favourite_title"):
        return flask.redirect("/register?errmsg=You didn't choose your favourite anime")
    
    username = flask.request.form.get("username")
    password = flask.request.form.get("password")
    confirmation = flask.request.form.get("password-confirmation")
    favouriteTitle = flask.request.form.get("favourite_title")

    print(password, confirmation)
    if help.CheckExisting(username):
        return flask.redirect("/register?errmsg=Such a username alredy exists")
    if password != confirmation:
        return flask.redirect("/register?errmsg=check password once more")
    
    return "Good job!"
    # load info to db
