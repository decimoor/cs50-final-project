import flask
import help
import sqlite3

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


@app.route("/register")
def register():
    # this route might get errmsg val which contains error message
    # if there is such a value function sends it to template, so user will see that
    errmsg = "No errors"
    if flask.request.args.get("errmsg"):
        errmsg = flask.request.args.get("errmsg")

    return flask.render_template("register.html")
    # just return register html file via flask.render_template function
    return errmsg
    # return flask.render_template("register.html", errmsg = errmsg)

@app.route("/registered")
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
    if not flask.request.form.get("confirmation"):
        return flask.redirect("/register?errmsg=You didn't confirm your password")

    # load info to db

