from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template('index.html')


# THIS TAKES FORM CONTENT FROM action="/process"
@app.route('/create/dojo', methods=["POST"])
def create():
    if not Dojo.validate(request.form):
        return redirect('/')

    Dojo.create_new(request.form)
    return redirect('/results')


@app.route('/results')
def results():

    return render_template('result.html', dojo=Dojo.get_last())


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
