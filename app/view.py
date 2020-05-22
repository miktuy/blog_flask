from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Mike'
    return render_template('index.html', name=name)


@app.route('/admin')
def open_admin():
    pass
