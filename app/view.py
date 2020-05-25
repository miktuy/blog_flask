from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Mike'
    return render_template('index.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/admin')
def open_admin():
    pass
