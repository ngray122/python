from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


DB = "dojo_survey_schema"


class Dojo:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        # create query we want to send to the database
        query = "SELECT * FROM dojos;"
        # create list that will store results of connectToMySQL function
        results = connectToMySQL
        # the parameter will be schema we created in MySQL.
        # .query_db allows query on the database using a string (query) we declared on line 16
        ('DB').query_db(query)

        all_dojos = []
        # for every index in results
        for row in results:
            # add index to Class list
            all_dojos.append(cls(dojo))
        # return dictionary
        return all_dojos

    @classmethod
    def create_new(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s );"
        result = connectToMySQL(DB).query_db(query, data)
        return result


    @classmethod
    def get_last(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(DB).query_db(query)
        return Dojo(results[0])


    @classmethod
    def select_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        return cls(result[0])


    @classmethod
    def edit(cls, data):
        query = "UPDATE dojos SET name = %(name)s, location= %(location)s, language=%(language)s, comment=%(comment)s WHERE dojos.id=%(id)s"
        return connectToMySQL(DB).query_db(query, data)



    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)



    @staticmethod
    def validate(dojo):
        is_valid = True 
        if len(dojo['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(dojo['location']) < 1:
            flash("You must choose a location from the dropdown menu.")
            is_valid = False
        if  len(dojo['language']) < 1:
            flash("You must choose a language from the dropdown menu.")
            is_valid = False
        if len(dojo['comment']) < 1:
            flash("Your comment must be more than 1 character long.")
            is_valid = False
        if len(dojo['comment']) > 500:
            flash("Your comment must be less than 500 characters.")
            is_valid = False
        return is_valid