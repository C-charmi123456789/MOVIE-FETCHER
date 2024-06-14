# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
from flask import request
import urllib.request
from urllib.parse import quote
import json

@app.route('/', methods=['GET', 'POST'])
def home():
    movies_data = None
    if request.method == 'POST':
        query = request.form.get('query')
        encoded_query = quote(query)
        with urllib.request.urlopen(f"https://api.watchmode.com/v1/autocomplete-search/?apiKey=TIX0aWcg37iGhy9i7RVpr54tcTKsKf01cCkmXMNX&search_value="+encoded_query+"&search_type=1") as url:
            movies_data = json.loads(url.read().decode())
            print(movies_data)
    return render_template('home.html', movies_data=movies_data)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0", port=5000, debug=True)