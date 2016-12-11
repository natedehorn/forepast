from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, DateField
import forepast

# App config.
SQLALCHEMY_TRACK_MODIFICATIONS = False
APP = Flask(__name__)
APP.config.from_object(__name__)
APP.config['SECRET_KEY'] = '_FbOqODzPCsqf583Dwvl8G0zH3'

class DateForm(Form):
    date = DateField()
 
@APP.route("/", methods=['GET', 'POST'])
def __main__():
    form = DateForm()
    if request.method == 'POST':
        if form.validate():
            if request.form['city'] and request.form['state']:
                print(request.form['date'], request.form['city'], request.form['state'])
                print(forepast.get((request.form['date'].translate(str.maketrans(' ', '/'))), request.form['city'], request.form['state']))
            if request.form['zipcode']:
                print(request.form['date'], request.form['zipcode'])
                city, state = forepast.ziptocity(request.form['zipcode'])
                print(forepast.get(request.form['date'], city, state))
    return render_template('index.html', form=form)

@APP.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == "__main__":
    APP.run(debug=True)