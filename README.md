    # Tennis Statistics
#### Video: https://youtu.be/JGtDaL3jTec
#### Description:

Tennis Statistics is a tracker that is a simple web application that allows tennis players to log match performance data and view statistics about their play over time. It was built using Python, Flask, SQLite, HTML and CSS.

The project was inspired by the need to easily record match stats such as winners, unforced errors, aces, double faults, and outcomes (wins/losses), track them over time then generate meaningful insights, that players may be able to use to improve performance.

---

## Features

- **Add Match**: Submit match data through a web form.
- **View Stats**: See total matches played, win/loss records, average stats per match, and most common opponents.
- **Persistent Storage**: Data is saved in a SQLite database.

---

## Project Structure

- `app.py`: The main Flask application. Contains all routes, database interactions with SQL and data processing logic for calculating averages and finding the most frequent opponent.
- `templates/`: Folder containing HTML files rendered by Flask using Jinja2 templating.
  - `index.html`: Home page with the form to add new match data.
  - `stats.html`: Displays calculated statistics and summaries.
- `static/styles.css`: The stylesheet that handles form layout, fonts, and button styles.
- `matches.db`: The database where match data is stored. One table was created called matches, which stored all the data.

---

## How It Works

On visiting the home page (`/`), the user sees a form to submit details from a match. Submitting the form sends a POST request to `/add`, which inserts the match into the database. Visiting `/stats` obtains the data from the SQL database for all matches and performs calculations: Win/loss totals and win percentage, averages for each tracked stat, and most frequent opponent(s) (with a tie-handling feature). The results are displayed in a HTML page 'stats.html'.

---

## Design Decisions

Flask was chosen for its suitability for small web projects. The Finance problem from the previous week seemed a good structure to base this on.
SQLite was selected because it stores the data long term. Also, I am interested in pursuing data science and hope to improve my SQL skills.
Python was used since it can combine SQL and flask. It is also relatively easy to calculate statistics using loops. Python was also used to deal with multiple opponents tieing for the most common opponent.
CSS was used to stle the webpages. I tried a tennis background but this made it difficult to read.

---

## Challenges Faced

- Choosing how to handle ties in common opponents. To begin with, I hadn't considered this possibility. It was only when I was writting the code to find the max_count I realised multiple opponents may have the same max_count. A list was created to contain all the opponents that had this max_count value, and an if statement was used to differentiate between one opponent being the most common or multiple opponents.
- Dealing with user input for wins/losses. It seemed like it may be complicated to deal with all the different errors users might make when entering wins and losses. To keep this simple, I dcided to instruct the user to just enter a single capatlized letter - W or L.
- Background image. A good amount of time was spent attempting to include a tennis background. This meant the rest of the text and layout had to be altered so it was still readable. Eventually I decided the image wasn't adding enough to justify the potential loss in useability.

---

## Possible Improvements

- Add login support so users can track stats individually.
- Include more options for data (surface type, first serve percentage etc)
- Better data visualisation using charts.

---

## Conclusion
Overall this project was a good way to bring together the skills I have gained during the course. I had never done any web design before, but had some experience with Python. I wanted to keep it relatively simple since this is my first web project from scratch. I am happy to have done some basic web design, but have realised I prefer other areas of computing. I have really enjoyed SQL and will look to learn more. 
