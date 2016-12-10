from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, DateField

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
            print(request.form['date'])
    return render_template('index.html', form=form)

@APP.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == "__main__":
    APP.run(debug=True)