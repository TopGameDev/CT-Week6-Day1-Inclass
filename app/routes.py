from app import app
from flask import render_template

# Add a route
@app.route('/')
def index():
    countries = ['United States', 'Canada', 'Mexico', 'France', 'Egypt', 'China']
    return render_template('index.html', first_name = 'Trevon', countries = countries)


@app.route('/signup')
def signup():
    return render_template('signup.html')