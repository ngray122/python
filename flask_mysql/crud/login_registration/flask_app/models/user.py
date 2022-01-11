from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash



class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']





# create new
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('login_and_registration_schema').query_db(query, data)
        print('Crete passed')
        return result



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('login_and_registration_schema').query_db(query, data)

        if len(result) == 0:
            return None
        else:
            return cls(result[0])
        


    @staticmethod
    def validate(data):
        is_valid = True
# does fn have at least 2 char
        if len(data['first_name']) < 3 or len(data
        # does fn have more than 255 char
        ['first_name']) > 255:
        # change the boollen variable is_valid to False 
            is_valid=False
            # and show this message to my user in the browser
            flash("Your first name must be between 3 and 255 characters lon. Please try again.")
        # if ln is less than 3 char
        if len(data['last_name']) < 3 or len(data['last_name']) > 255:
        # change boolean to false
            is_valid=False
            # and display this to the user
            flash("Your last name must be between 3 and 255 characters long. Please try again.")
        # EX.match function is checking 
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("The email you entered is invaild.  It must be between ")
        
        elif User.get_one(data) != None:
            is_valid = False
            flash('Email is already in use')
        
        if len(data['password']) < 8 or len(data['password']) > 59:
            is_valid=False
            flash("Password should be 8 to 60 characters long")
        elif len(data['password']) == 0:
            is_valid=False
            flash("You must choose a password")

        if data['password'] != data['confirm_password']:
            is_valid=False
            flash("Passwords must match")
        
        return is_valid