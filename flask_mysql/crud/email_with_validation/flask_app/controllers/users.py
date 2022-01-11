from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import Email


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/success')
def display():
    emails = Email.get_all()
    return render_template("/success.html", emails=Email.get_all(), )


@app.route('/create/email', methods=['POST'])
def create():

    if not Email.validate(request.form):
        return redirect('/')
  
    Email.create_new(request.form)
    return redirect("/success")


@app.post('/delete')
def delete(id):
    data = {
        'id': id
    }
    Email.delete(data)
    return redirect('/index.html')


