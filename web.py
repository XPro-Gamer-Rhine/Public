from flask import Flask, render_template
import json
import pandas as pd
import csv

app = Flask(__name__)


@app.route('/')
def index():
    results = []
    with open("All Data.csv") as csvfile:
      reader = csv.reader(csvfile)
    
      for row in reader:
          results.append(row)
    return render_template("table.html",title='Crypto Currency Data',data=results)
    

if __name__ == '__main__':
  
  app.run(debug=True)