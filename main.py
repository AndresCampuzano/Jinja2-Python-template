from flask import Flask, request, make_response, escape, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    first_name = "Andres"
    stuff = "This is <strong>bold text</strong>"
    pizzas = ["pepperoni", "cheese", "another pizza", 41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           pizzas=pizzas)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
                           name=name,
                           form=form)


# Create custom error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
