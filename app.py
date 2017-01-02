from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, DateField
import forepast
import json

# App config.
SQLALCHEMY_TRACK_MODIFICATIONS = False
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '_FbOqODzPCsqf583Dwvl8G0zH3'

class DateForm(Form):
    date = DateField()
 
@app.route("/", methods=['GET', 'POST'])
def __main__():
    form = DateForm()
    if request.method == 'POST':
        if form.validate():
            if request.form['date']:
                date = request.form['date']
                if request.form['city'] and request.form['state']:
                    city = request.form['city']
                    state = request.form['state']
                    print(date, city, state)
                    full = forepast.get(date, city, state)
                    print(full)
                    summary = full.get('history').get('observations')
                    '''[d['value'] for d in summary]'''
                    return render_template('index.html', form=form, data=summary)
                if request.form['zipcode']:
                    zipcode = request.form['zipcode']
                    print(date, zipcode)
                    city, state = forepast.ziptocity(zipcode)
                    print(forepast.get(date, city, state))
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)