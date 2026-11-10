from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
import statistics


# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tennis.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    opponent = request.form.get("opponent")
    result = request.form.get("result").upper()
    winners = int(request.form.get("winners"))
    unforced_errors = int(request.form.get("unforced_errors"))
    aces = int(request.form.get("aces"))
    double_faults = int(request.form.get("double_faults"))

    db.execute("INSERT INTO matches (opponent, result, winners, unforced_errors, aces, double_faults) VALUES (?,?,?,?,?,?)", opponent, result, winners, unforced_errors, aces, double_faults)

    return redirect("/stats")

@app.route("/stats")
def stats():
    matches = db.execute("SELECT opponent, result, winners, unforced_errors, aces, double_faults FROM matches")
    if not matches:
        return render_template("stats.html", total=0)

    wins, winners, unforced_errors, aces, double_faults = 0,0,0,0,0
    opponents = []
    for match in matches:
        if match["result"] =="W":
            wins += 1
        winners += match["winners"]
        unforced_errors += match["unforced_errors"]
        aces += match["aces"]
        double_faults += match["double_faults"]
        opponents.append(match["opponent"])

    total = len(matches)
    losses = total - wins

    avg_winners = round(winners / total, 1)
    avg_unforced_errors = round(unforced_errors / total, 1)
    avg_aces = round(aces / total, 1)
    avg_double_faults = round(double_faults / total, 1)
    win_percent = round((wins / total) * 100, 1)
    counts = {}

    for opponent in opponents:
        if opponent in counts:
            counts[opponent] += 1
        else:
            counts[opponent] = 1

    if not counts:
        common_opp = "N/A"
    else:
        max_count = 0
        for count in counts.values():
            if count > max_count:
                max_count = count

        common_opponents = []
        for opponent in counts:
            if counts[opponent] == max_count:
                common_opponents.append(opponent)

        if len(common_opponents) == 1:
            common_opp = common_opponents[0]
        else:
            common_opp = ", ".join(common_opponents) + f" (tied at {max_count} matches each)"

    return render_template("stats.html",
                       total=total,
                       wins=wins,
                       losses=losses,
                       win_percent=win_percent,
                       avg_winners=avg_winners,
                       avg_unforced_errors=avg_unforced_errors,
                       avg_aces=avg_aces,
                       avg_double_faults=avg_double_faults,
                       common_opp=common_opp)

