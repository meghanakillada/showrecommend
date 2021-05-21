"""Python"""
from flask import Flask, render_template, request
import random
import requests
import json

app = Flask(__name__)

#popular tv shows api call from "Episodate"
url = "https://www.episodate.com/api/most-popular?page=1"
response = requests.request("GET", url)

#json output to python dictionary
responseJsonObj = json.loads(response.text)

#appending dictionary items into a list
libraryList = []
for data in responseJsonObj['tv_shows']:
    libraryList.append(data['name'])

showList =[]

def ShowRecommendations(series):
    #validation
    if series < 0 or series > 20:
        raise ValueError("Number must be between 0 and 20")
    #initialization
    showList = []
    #build a random data list
    f = [random.sample((libraryList), k=series)]
    showList.append(f[0])
    return showList

#routing
@app.route('/')
@app.route('/minilab', methods=["GET", "POST"])
def minilab():
    if request.method == 'POST':
        n = int(request.form.get("shows"))
        return render_template("minilab.html", showrecs=ShowRecommendations(n), inputvalue=n)
    else:
        #default is 1
        return render_template("minilab.html", showrecs=ShowRecommendations(1), inputvalue=1)

#runs the application
if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')