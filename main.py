from flask import Flask
from flask import render_template
from flask import request
from flask import Flask
from secret import API_KEY

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=API_KEY)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        titles = []
        descriptions = []
        urls = []
        amounts = int(request.form["amount"])
        key = request.form["Location"] + " " + request.form["Keywords"]
        top_headlines = newsapi.get_everything(q=key)["articles"][:amounts]
        for i in range(len(top_headlines)):
            titles.append(top_headlines[i]["title"])
            descriptions.append(top_headlines[i]["description"])
            urls.append(top_headlines[i]["url"])
        return render_template("main.html", title=titles, description=descriptions, url=urls, amount=amounts)
    else:
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
    