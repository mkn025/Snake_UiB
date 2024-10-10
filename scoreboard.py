from flask import Flask, render_template
import csv

app = Flask(__name__)

# låns inspirasjon og deler av fra stackoverflow og flask scoreboard se README.md 
# har også litt erfaring med flask fra tidligere prosjekter

def read_scoreboard(): 
    scoreboard = []
    with open('comp/scoreboard.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scoreboard.append(row)
    return scoreboard

@app.route('/')
def index():
    scoreboard = read_scoreboard()
    return render_template('scoreboard.html', scoreboard=scoreboard)

if __name__ == '__main__':
    app.run(debug=True)