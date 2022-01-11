from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key="this is a secret"


@app.route('/', methods=["GET", "POST"])
def signIn():

    if request.method == "POST":
        req = request.form
        username= req.get("username")
        password = req.get("password")

        print(username, password)



    return render_template('/')



if __name__ == '__main__':
    app.run(debug = True, port = 5001)