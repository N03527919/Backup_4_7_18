#!/usr/bin/python

from flask import Flask, render_template
import datetime
app = Flask(__name__)
import time

@app.route("/")
def hello():
  while (True):
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
      'title' : 'HELLO!',
      'time' : timeString
    }
    return render_template('main.html',**templateData)
    sleep(1)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 8081, debug = True)
