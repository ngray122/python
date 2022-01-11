from flask import render_template, request, redirect, session, flash
from flask_app.models.show_model import Show
from flask_app.models.user_model import User
from flask_app import app


@app.route('/dashboard')
def get_all_shows():
    if 'user_id' not in session:
        flash('This page only available if logged in, please log in')
        return redirect('/')
    else:
        shows = Show.get_all_shows()
        return render_template('/dashboard.html', shows=shows)



@app.route('/create/show')
def create_page():
    return render_template('create.html' )




#when using POST method, always make secong route for read.  never render template on POST
@app.route('/create', methods=['POST'])
def create_new_show():
    if 'user_id' not in session:
        flash('This page only available if logged in')

    if Show.validate(request.form):
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'date': request.form['date'],
            'user_id': session['user_id']

        }

        Show.create_new_show(data)

        return redirect('/dashboard')
    return redirect('/create/show')








@app.route('/show/<int:id>')
def show_single_show(id):
    # creating data dict to pass in key query is looking for 
    data = {
        'id': id
    }
    #creatign variable that can access data from one row by ID (get_one(data))
    one_show = Show.get_one(data)
    # to use to render our html onto our template
    return render_template('show.html', one_show=one_show)








# view edit page
@app.route('/edit/<int:id>/show')
def view_edit(id):
    # creating data dict to pass in key id that my query is looking for
    data = {
        'id': id
    }
    # calling my Recipe class using the get one method I made
    # and putting that recipe into a variable to pass into my html
    show = Show.get_one(data)
    return render_template('edit.html', show=show)





# edit
@app.route('/edit/<int:id>', methods=["POST"])
def edit_single_show(id):
    if 'user_id' not in session:
        flash('This page only available if logged in')

    #check if Class.request.form information is valid
    if Show.validate(request.form):
    # create data dictionary from from to edit recipe
        data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'date': request.form['date'],
            'id': id
        }
        #call edit single method I just made on Recipe class
        Show.edit_single_show(data)
        print(Show)

        return redirect('/dashboard')
    # redirect to edit page if not in session (watch the indentaion!!) 
    return redirect(f'/edit/{id}/show')




#delete item by id#
@app.route('/delete/<int:id>')
def delete_item(id):
    data = {
        'id': id
    }
    # class recipe delete item data which is = to (id)
    Show.delete_item(data)
    return redirect('/dashboard')