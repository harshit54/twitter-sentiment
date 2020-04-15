from flask import Flask, render_template, request, url_for
from .twitter_analysis import analyze

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route('/next', methods=["POST", "GET"])
def success():
    search_string = request.form.get('search')
    if request.method == 'GET':
        return render_template('index.html')
    else:
        sentiment = analyze(search_string)
        if sentiment == -2:
            return render_template("error.html", error="Can't find enough Tweets.")
        if sentiment >= 0:
            color = 'Green'
        else:
            color = 'Tomato'
        return render_template("next.html", keyword = search_string, color = color, sentiment_value = sentiment)
