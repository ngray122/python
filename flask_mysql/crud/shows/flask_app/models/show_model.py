from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
from flask_app.models.user_model import User



class Show:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.date = data['date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None



    @classmethod
    def get_all_shows(cls):

        query = "SELECT * FROM shows JOIN users ON user_id WHERE shows.user_id = users.id;"
        results = connectToMySQL('shows_schema').query_db(query)
        # create list for db table dictionaries
        shows = []
        # for row in query results
        for row in results:
            new_show = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            show_user = User(user_data)
            new_show.user = show_user
            shows.append(new_show)
        return shows




    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        result = connectToMySQL('shows_schema').query_db(query, data)
        single_show = cls(result[0])
        return single_show




    @classmethod
    def create_new_show(cls, data):
        query = "INSERT INTO shows (name, description, date, user_id) VALUES (%(name)s, %(description)s, %(date)s, %(user_id)s);"

        result = connectToMySQL('shows_schema').query_db(query, data)
        return result





    @classmethod
    # edit does not need to be returned
        # selecting update by id
    def edit_single_show(cls, data):
        query = "UPDATE shows SET name=%(name)s, description= %(description)s, date = %(date)s WHERE id = %(id)s;"
        connectToMySQL('shows_schema').query_db(query, data)





    @classmethod
    #from id
    def delete_item(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        result = connectToMySQL('shows_schema').query_db(query, data)






    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 3:
            is_valid = False
            flash("Name must be 2 or more characters long")

        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be 2 or more characters long")

        elif len(data['date']) != 10:
            is_valid = False
            flash("A valid date must be entered!")

        return is_valid