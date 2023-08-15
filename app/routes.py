from app import app
from flask import render_template
from app.forms import SignUpForm


# Add a route
@app.route('/')
def index():
    countries = ['United States', 'Canada', 'Mexico', 'France', 'Egypt', 'China']
    return render_template('index.html', first_name = 'Trevon', countries = countries)


@app.route('/signup')
def signup():
    form = SignUpForm()
    print(form.first_name)
    return render_template('signup.html', form=form)