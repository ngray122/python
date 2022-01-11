from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'its a secret'


@app.route('/')
def index():

    if 'link' not in session:
        session['link'] = 0
    else:
        session['link']+=1
    return render_template('index.html', link=str('link'))


if __name__ == '__main__':
    app.run(debug=True)