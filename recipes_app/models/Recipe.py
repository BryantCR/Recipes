from recipes_app.config.MySQLConnection import connectToMySQL
from recipes_app import app 
from datetime import date, datetime
from flask import flash
from flask import render_template, request, redirect, session



class Recipe:
    def __init__(self, recipes_id, recipe_name, description, recipe_instructions, thirty_minutes, created_at, updated_at):
        self.recipes_id = recipes_id
        self.recipe_name = recipe_name
        self.description = description
        self.recipe_instructions = recipe_instructions
        self.thirty_minutes = thirty_minutes
        self.created_at = created_at
        self.updated_at = updated_at
        self.User = []

    @classmethod
    def add_new_recipe (cls, data):
        query = "INSERT INTO recipes (recipe_name, description, recipe_instructions, thirty_minutes, created_at, updated_at) VALUES ( %(recipe_name)s , %(description)s , %(recipe_instructions)s, %(thirty_minutes)s, %(created_at)s, SYSDATE());"
        data2 = {
            "recipe_name" : data[0],
            "description" : data[1],
            "recipe_instructions" : data[2],
            "thirty_minutes" : data[3],
            "created_at" : data[4],
        }
        result = connectToMySQL('recipes_schema').query_db( query, data2 )

        query = "INSERT INTO users_recipes (user_users_id, recipe_recipes_id) VALUES ( %(user_users_id)s , %(recipe_recipes_id)s );"
        data3 = {
            "user_users_id" : session['users_id'],
            "recipe_recipes_id" : result
            }
        connectToMySQL('recipes_schema').query_db( query, data3 )
        return result

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT recipes.recipe_name, recipes.description, recipes.recipe_instructions, recipes.thirty_minutes, recipes.created_at, recipes.recipes_id, users.users_id, users.first_name FROM users JOIN users_recipes ON users.users_id = users_recipes.user_users_id JOIN recipes ON recipes.recipes_id = users_recipes.recipe_recipes_id;"
        #query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes_schema').query_db( query )
        return results

    @classmethod
    def get_recipe_information( cls, id ):
        query = "SELECT * FROM recipes WHERE recipes_id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL('recipes_schema').query_db( query, data )
        return result

    @classmethod
    def delete_recipe(cls, id ):
        data = {
            "id" : id
        }
        query = "DELETE FROM users_recipes WHERE recipe_recipes_id = %(id)s;"
        result1 = connectToMySQL('recipes_schema').query_db( query, data )

        query = "DELETE FROM recipes WHERE recipes_id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db( query, data )
        return result, result1

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET recipe_name = %(recipe_name)s, description=%(description)s, recipe_instructions = %(recipe_instructions)s , thirty_minutes = %(thirty_minutes)s, created_at = %(created_at)s, updated_at = SYSDATE() WHERE recipes_id = %(recipes_id)s;"

        updateData = {
            'recipe_name' : data[0],
            'description' : data[1],
            'recipe_instructions' : data[2],
            'thirty_minutes' : data[3],
            'created_at' : data[4],
            'recipes_id' : data[5]
        }
        
        results = connectToMySQL('recipes_schema').query_db( query, updateData )
        #query = "UPDATE recipes SET recipe_name = %(recipe_name)s, description=%(description)s, recipe_instructions = %(recipe_instructions)s , thirty_minutes = %(thirty_minutes)s, created_at = %(created_at)s, updated_at = SYSDATE() WHERE recipes_id = %(recipes_id)s;"

        # updateData = {
        #     'recipes_id' : data[0],
        #     'recipe_name' : data[1],
        #     'description' : data[2],
        #     'recipe_instructions' : data[3],
        #     'thirty_minutes' : data[4],
        #     'created_at' : data[5],
        # }
        
        # results = connectToMySQL('recipes_schema').query_db( query, updateData )
        return results


#################################################################################


    @staticmethod
    def validate_recipe(data):
        isValid = True
        query = "SELECT * FROM recipes WHERE users_id = %(users_id)s;"
        data2 = {
            "recipe_name" : data[0],
            "description" : data[1],
            "recipe_instructions" : data[2],
            "created_at" : data[3],
            "thirty_minutes" : data[4],
        }
        results = connectToMySQL('recipes_schema').query_db( query, data2 )

        if len(results) == 1:
            flash("Email already registered")
            isValid = False
        if len( data[0] ) < 2:
            flash( "First name must be at least 2 characters long" )
            isValid = False 
        if len( data[1] ) < 2:
            flash( "Last name must be at least 2 characters long")
            isValid = False
        if not EMAIL_REGEX.match(data[2]):
            flash("Email Address must have a valid format, try with a new one please")
            isValid = False
        if len(data[3]) < 8:
            flash("Password must be at least 8 characters long")
            isValid = False
        if data[3] != data[5]:
            flash("Passwords must match, try again")
            isValid = False
        return isValid

    @staticmethod
    def validate_Create_Recipe(data):
        isValid = True
        if len(data[0]) < 3:
            flash("The Name must be at least 3 characters long")
            isValid = False
        if len(data[1]) < 3:
            flash("The description must be at least 3 characters long")
            isValid = False
        if len(data[2]) < 3:
            flash("The instructions must be at least 3 characters long")
            isValid = False
        # if data[3] == '':
        #     flash("You must check the time")
            isValid = False
        if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0:
            flash("There is an empty data space try to fill it")
            isValid = False
        return isValid

    @staticmethod
    def validate_Update_Recipe(data):
        isValid = True
        if len(data[0]) < 3:
            flash("The Name must be at least 3 characters long")
            isValid = False
        if len(data[1]) < 3:
            flash("The description must be at least 3 characters long")
            isValid = False
        if len(data[2]) < 3:
            flash("The instructions must be at least 3 characters long")
            isValid = False
        if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0:
            flash("There is an empty data space try to fill it")
            isValid = False
        return isValid
