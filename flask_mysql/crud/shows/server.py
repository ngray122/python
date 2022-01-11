from flask_app import app
# import controllers
from flask_app.controllers import users
from flask_app.controllers import shows_cont



if __name__ == '__main__':
    app.run(debug=True, port=5001)