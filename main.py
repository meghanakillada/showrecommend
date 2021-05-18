"""Create Task"""
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

#appending dictonary items into a list
showList1 = []
for data in responseJsonObj['tv_shows']:
    showList1.append(data['name'])
n = 1

#creating a class
class Shows:
    #initialization
    def __init__(self, series):
        #validation
        if series < 0 or series > 20:
            raise ValueError("Series must be between 0 and 20")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.show_series()

    #function to build a random data list
    def show_series(self):
        limit = self._series
        #starting array/list
        f = [random.sample((showList1), k=self.series)]
        #calls "set_data"
        self.set_data(f[0])

    #function to set the list and the dictionary
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    #getters enable class variables to be called outside of class
    @property
    def series(self):
        return self._series
    @property
    def list(self):
        return self._list
    @property
    def number(self):
        return self._list[self._dictID - 1]
    def get_sequence(self, nth):
        return self._dict[nth]

#routing
@app.route('/')
@app.route('/minilab', methods=["GET", "POST"])
def minilab():
    if request.method == 'POST':
        n = int(request.form.get("shows"))
        return render_template("minilab.html", showrecs=Shows(n))
    else:
        #default is 1
        return render_template("minilab.html", showrecs=Shows(1))

#runs the application
if __name__ == "__main__":
    app.run(port='3000', host='127.0.0.1')