from flask import render_template, request, redirect, session
from flask_app.models.paint_model import Painting
from flask_app.models.user import User
from flask_app.controllers import users
from flask_app import app
from flask import flash


@app.route('/dashboard')
def get_all_paintings():
    if 'user_id' not in session:
        flash('This page only available if logged in')
        return redirect('/')
    else:
        paintings = Painting.get_all_paintings()
        return render_template('dashboard.html', paintings=paintings)



@app.route('/create/painting')
def create_page():
    return render_template('create.html')


#when using POST method, always make secong route for read.  NEVER render template on POST
@app.route('/create', methods=['POST'])
def create_new_painting():
    if 'user_id' not in session:
        flash('This page only available if logged in')

    if Painting.validate(request.form):
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'user_id': session['user_id']

        }

        Painting.create_new_painting(data)

        return redirect('/dashboard')
    return redirect('/create/painting')



@app.route('/show/<int:id>')
def show_painting(id):
    data = {
        'id': id
    }
    one_painting = Painting.get_one(data)
    return render_template('show.html', one_painting=one_painting)




@app.route('/edit/<int:id>/painting')
def view_edit(id):
    
    data = {
        'id': id
    }
    
    painting = Painting.get_one(data)
    return render_template('edit.html', painting=painting)



# edit
@app.route('/edit/<int:id>', methods=["POST"])
def edit_single_painting(id):
    if 'user_id' not in session:
        flash('This page only available if logged in')

    #check if Class.request.form information is valid
    if Painting.validate(request.form):
    # create data dictionary from from to edit painting
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'id': id
        }
        Painting.edit_single_painting(data)
        print(Painting)

        return redirect('/dashboard')
    # redirect to edit page if not in session (watch the indentaion!!) 
    return redirect(f'/edit/{id}/painting')



@app.route('/delete/<int:id>')
def delete_item(id):
    data = {
        'id': id
    }
    
    Painting.delete_item(data)
    return redirect('/dashboard')