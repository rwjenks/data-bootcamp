# ## Mission To Mars
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scraper

# Setup Flask App
app = Flask(__name__)

client = pymongo.MongoClient()

@app.route("/")
def index():
    mars = db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars= db.mars
    data = scraper.scrape()
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)