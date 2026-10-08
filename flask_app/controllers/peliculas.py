from flask_app import app
from flask import render_template

@app.route('/cine')
def cine():
    return render_template('cine.html')