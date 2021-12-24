from re import match
import flask
import flask_session
import help
import sqlite3
import m_imdb
import json

sqliteConnection = sqlite3.connect("anime.db")

app = flask.Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
flask_session.Session(app)

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
    return flask.render_template("main.html")   


# get anime list function
@app.route("/getAnimeList", methods=["GET", "POST"])
def getAnimeList():
    titleName = flask.request.args.get("titleName")
    matchesTitles = m_imdb.GetAnimeList(titleName)
    print(matchesTitles)
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
        return flask.redirect("/register?errmsg=Check password once more")
    if password in ["Alim", "Petya"]:
        flask.redirect("/register?errmsg=Your names sucks pls change")
    # load info to db
    help.AddRowToUserTable(name = username, password = password, favourite_title = favouriteTitle)
    flask.session["id"] = help.GetUserId(username)
    return flask.redirect(f"/?user_id={help.GetUserId(username)}")

@app.route("/login", methods = ["POST", "GET"])
def Login():
    errmsg = "No errors"
    if flask.request.args.get("errmsg"):
        errmsg = flask.request.args.get("errmsg")

    return flask.render_template("login.html", errmsg = errmsg)

@app.route("/loginned", methods = ["GET", "POST"])
def Loginned():
    # check if user didn't type neither username nor password
    if not flask.request.form.get("username") and not flask.request.form.get("password"):
        return flask.redirect("/login?errmsg=You didn't write any info!!!")
    # check if user didn't type his username
    if not flask.request.form.get("username"):
        return flask.redirect("/login?errmsg=You didn't enter your username")
    # check if user didn't type his password
    if not flask.request.form.get("password"):
        return flask.redirect("/password?errmsg=You didn't enter your password")
    
    username = flask.request.form.get("username")
    password = flask.request.form.get("password")

    # check if there is a registered user with exactly same password and username
    if help.CheckExisting(username) and help.CheckPassword(username, password):
        flask.session["id"] = help.GetUserId(username)
        return flask.redirect("/")

    return flask.render_template("login.html", errmsg = "You entered wrong password")


@app.route("/getTitles", methods = ["POST", "GET"])
def GetTitles():
    if flask.request.form.get("mode") == "unwatched":
        # !!! this is debug version of the function !!!
        # the proper version of function looks this wat
        # help.GetUnwatchedTitles(flask.session["user_id"])
        return str(help.GetUnwatchedTitles(1))
    # !!! this is debug version of the function !!!
    # the proper version of function looks this way
    # watchedTitles = help.GetWatchedTitles(flask.session["user_id"])
    watchedTitles = help.GetWatchedTitles(1)
    print(watchedTitles)
    return json.dumps(watchedTitles)



@app.route("/AddTitle", methods = ["POST", "GET"])
def AddTitle():
    
    
    # Title's layout
    # [0] - id
    # [1] - name
    # [2] - picture's url
    # [3] - tags


    # check if there is title's name
    if not flask.request.form.get("titleName"):
        return flask.redirect("/main?errmsg=You didn't wrote titleName")
    
    titleInfo = help.GetTitle(flask.request.form.get("titleName"))
    # check if there is a rating and description (available only if it's watched title)
    if flask.request.form.get("mode") == "watched":
        if not flask.request.form.get("rating"):
            return flask.redirect("/main?errmsg=You didn't select rating")
        if not flask.request.form.get("description"):
            return flask.redirect("/main?errmsg=You didn't write description")
        # adding this title to user's watched titles database
        title = {
            "id": titleInfo[0],
            "name": titleInfo[1],
            "rating": int(flask.request.form.get("rating")),
            "description": flask.request.form.get("description")
        }
        help.AddToWatchedTitles(title)
        return "Successfully added title to watched titles"
    if flask.request.form.get("mode") == "unwatched":
        title = {
            "id": titleInfo[0],
            "name": titleInfo[1],
        }
        # debug version
        help.AddToUnwatchedTitles(title, 4)
        # release version
        # help.AddToUnwatchedTitles(title, session["user_id"])
        return "Successfully added title to unwatched titles"
