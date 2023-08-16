from app import app, db
from flask import render_template, redirect, url_for
from app.forms import SignUpForm, PostForm
from app.models import User, Post
from flask_login import login_user, logout_user


# Add a route
@app.route('/')
def index():
    posts = db.session.execute(db.select(Post).order_by(Post.date_created.desc())).scalars().all()
    countries = ['United States', 'Canada', 'Mexico', 'France', 'Egypt', 'China']
    return render_template('index.html', first_name = 'Trevon', countries = countries, posts=posts)


@app.route('/signup', methods=['GET', "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        #Get the data from the form
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)


        #Check user table to see if there are any users with username or email
        check_user = db.session.execute(db.select(User).where((User.username==username) | (User.email==email))).scalar()
        if check_user:
            print('A user with that username already exists')
            return redirect(url_for('signup'))
        
        # Create a new instance of the User class with the data from form
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

        # Add the new_user objects to the database
        db.session.add(new_user)
        db.session.commit()

        # Log the user in
        login_user(new_user)

        # Redirect to the homepage
        return redirect(url_for('index'))


    return render_template('signup.html', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        image_url = form.image_url.data or None
        print(title, body, image_url)

        # Create a new post instance
        new_post = Post(title=title, body=body, image_url=image_url, user_id=1)

        # Add that object to the Table
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))