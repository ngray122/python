from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Email:
    def __init__(self, data):

        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email_addresses";
        emails = []
        results = connectToMySQL("user_emails").query_db(query)
        for email in results:
            emails.append(cls(email))
        return emails


    @classmethod
    def create_new(cls, data):
        query = "INSERT INTO email_addresses (email) VALUES (%(email)s);"
        result = connectToMySQL(
            "user_emails").query_db(query, data)
        return result


    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM email_addresses WHERE id = %(id)s"
        result = connectToMySQL("user_emails").query_db(query, data)
        return cls(result[0])


    @classmethod
    def edit_existing(cls, data):
        query = "UPDATE email_addresses SET email = %(email)s WHERE user.id=%(id)s"
        return connectToMySQL("user_emails").query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM email_addresses WHERE id = %(id)s;"
        return connectToMySQL("user_emails").query_db(query, data)


   
    @staticmethod
    def validate(email):
        is_valid = True
        query = "SELECT * FROM email_addresses WHERE email = %(email)s;"
        results = connectToMySQL("user_emails").query_db(query,email)

        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email, choose new email")
            is_valid=False
        return is_valid