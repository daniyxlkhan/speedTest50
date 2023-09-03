import speedtest

from cs50 import SQL
from colorama import Fore, init
from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

from helper import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///speedtest.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    init(
        autoreset=True
    )  # Console colors will automatically reset to default after the last Colorama command has been invoked

    print(
        Fore.GREEN
        + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED....."
    )

    # initializing the SpeedTest instance
    st = (
        speedtest.Speedtest()
    )  # creating an instance of the Speedtest class from the speedtest module

    st.get_best_server()  # Get the most optimal server available
    st.download()  # Get downloading speed
    st.upload()  # Get uploading Speed

    # Save all these elements in a dictionary
    res_dict = st.results.dict()

    # Assign to variables with an specific format

    download_speed_bps = res_dict["download"]  # Download speed in bits per second (bps)
    upload_speed_bps = res_dict["upload"]  # Upload speed in bits per second (bps)

    # Convert to megabits per second (Mbps)
    download_speed_mbps = download_speed_bps / 100000000
    upload_speed_mbps = upload_speed_bps / 100000000

    # Round to two decimal places
    download_speed = round(download_speed_mbps, 2)
    upload_speed = round(upload_speed_mbps, 2)

    ping = round(res_dict["ping"], 2)
    latency = round(res_dict["ping"], 2)
    sponsor = res_dict["server"]["sponsor"]

    if "user_id" in session:
        db.execute(
            "INSERT INTO history(username, user_id, download_speed, upload_speed, ping, latency, sponsor) VALUES(:username, :user_id, :download_speed, :upload_speed, :ping, :latency, :sponsor)",
            username=session["username"],
            user_id=session["user_id"],
            download_speed=download_speed,
            upload_speed=upload_speed,
            ping=ping,
            latency=latency,
            sponsor=sponsor,
        )

    return render_template(
        "test.html",
        download_speed=download_speed,
        upload_speed=upload_speed,
        ping=ping,
        sponsor=sponsor,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE name = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash_pass"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["name"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmation")
        name_check = db.execute(
            "SELECT name FROM users WHERE name = :username", username=username
        )

        if not username or not password or not confirm_password:
            return apology("Missing Username or/and password")
        elif password != confirm_password:
            return apology("Passwords are not the same!")
        elif len(name_check) > 0:
            return apology("Username Already Exists")
        else:
            hash_password = generate_password_hash(password)
            db.execute(
                "INSERT INTO users(name, hash_pass) VALUES(:username, :hash_password)",
                username=username,
                hash_password=hash_password,
            )
            return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    # Remove user id from session
    session.clear()
    # Redirect user to home page
    return redirect("/")


@app.route("/history")
@login_required
def history():
    results = db.execute(
        "SELECT test_number, download_speed, upload_speed, ping, latency, sponsor FROM history WHERE user_id = :user_id",
        user_id=session["user_id"],
    )
    return render_template("history.html", results=results)


@app.errorhandler(500)
def internal_server_error(e):
    return "500 Internal Server Error - Something went wrong.", 500
