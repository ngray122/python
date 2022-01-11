from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash




class Painting:

    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None



    @classmethod
    def get_all_paintings(cls):

        query = "SELECT * FROM paintings JOIN users ON user_id WHERE paintings.user_id = users.id;"
        results = connectToMySQL('paintings_schema').query_db(query)
        # create list for db table dictionaries
        paintings = []
        # for row in query results
        for row in results:
            new_painting = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            painting_user = User(user_data)
            new_painting.user = painting_user
            paintings.append(new_painting)
        return paintings



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM paintings WHERE id = %(id)s;"
        result = connectToMySQL('paintings_schema').query_db(query, data)
        one_painting = cls(result[0])
        return one_painting




    @classmethod
    def create_new_painting(cls, data):
        query = "INSERT INTO paintings (name, description, price, user_id) VALUES (%(name)s, %(description)s, %(price)s, %(user_id)s);"

        result = connectToMySQL('paintings_schema').query_db(query, data)
        return result


    @classmethod
    # edit does not need to be returned
        # selecting update by id
    def edit_single_painting(cls, data):
        query = "UPDATE paintings SET name=%(name)s, description= %(description)s, price=%(price)s WHERE id = %(id)s;"
        connectToMySQL('paintings_schema').query_db(query, data)


    @classmethod
    #from id
    def delete_item(cls, data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        result = connectToMySQL('paintings_schema').query_db(query, data)



# I could not figure out how to validate my int.....
    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 3:
            is_valid = False
            flash("Name must be 2 or more characters long")

        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be 2 or more characters long")

        elif len(data['price']) < 1 :
                # was not able to validate if 'price value < 0' , edited on HTML input instead
            # and int(data['price']) < 0???

            is_valid = False
            flash("You must enter valid a price point!")

        return is_valid