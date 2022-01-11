from flask import Flask, render_template, request, session, redirect
import random

# 
app = Flask(__name__)
app.secret_key = 'this is a secret'



@app.route('/',methods=["POST"])
def index():
    if "random_number" not in session:
        session['random_number'] = random.randint(1, 101)


    return render_template('index.html')


@app.route('/guess', methods=["POST"])
def guess():
    session['player_guess'] = int(request.form['player_guess'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
