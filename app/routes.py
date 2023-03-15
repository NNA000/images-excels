from flask import render_template
from app import app


class HomeApp:
    def home(self):
        return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')