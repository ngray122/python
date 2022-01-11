from flask import Flask, render_template, request
app = Flask(__name__)

# routes go here

# GET a GET request, for data from the server
 #POST a POST request, when we send data to the server (typically via a form)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hande_information", methods=["POST"])
def handle_info():
    print(request.form["maiden_name"])
    return "done!"

if __name__ == '__main__':
    app.run(debug = True, port = 5001)



