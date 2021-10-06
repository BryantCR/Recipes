from flask import render_template, request, redirect, session
from recipes_app import app
from flask_bcrypt import Bcrypt
from flask import flash
from recipes_app.models.Recipe import Recipe
from recipes_app.models.User import User
import re


@app.route('/recipe/add', methods = ['POST'] )#receive the data an does the add 
def addnNewRecipe():
    print("ROUTE /recipe/add, addnNewRecipe ==> ( ['POST'] ) in excecution*****************")
    recipe_name = request.form['recipe_name']
    description = request.form['description']
    recipe_instructions = request.form['recipe_instructions']
    thirty_minutes = request.form['thirty_minutes']
    created_at = request.form['created_at']

    data = (recipe_name, description, recipe_instructions, thirty_minutes, created_at)
    print("FROM FORM 2 ADD RECIPE: ", data )
    # Recipe.add_new_recipe(data)
    # return redirect('/dashboard')
    if Recipe.validate_Create_Recipe(data):
        Recipe.add_new_recipe(data)
        flash("Created successfull")
        return redirect('/dashboard')
    else:
        print("invalid values")
    return redirect('/recipes/new')

@app.route("/recipes/<id>")
def showrecipedata(id):
    data = {
        'users_id': session['users_id'],
        'id' : id
    }
    # result = Recipe.get_recipe_information(id)
    result = Recipe.get_recipe_information(id)
    users = User.get_userBy_id(data)
    return render_template("instructions.html", userwall = users, recipe = result )

@app.route("/recipes/edit/<id>", methods = ['GET'])
def editRecipes(id):
    data = {
        'users_id': session['users_id'],
        'id' : id
    }
    users = User.get_userBy_id(data)
    result = Recipe.get_recipe_information(id)
    return render_template( "editrecipe.html", userwall = users, data = result)

@app.route('/recipe/edit', methods = ['POST'] )#receive the data an does the add 
def editRecipe():
    print("ROUTE /recipe/add, editRecipe ==> ( ['POST'] ) in excecution*****************")
    recipe_name = request.form['updaterecipe_name']
    description = request.form['updatedescription']
    recipe_instructions = request.form['updaterecipe_instructions']
    thirty_minutes = request.form['updatethirty_minutes']
    created_at = request.form['updatecreated_at']
    recipes_id = request.form['recipes_id']

    data = (recipe_name, description, recipe_instructions, thirty_minutes, created_at,recipes_id)
    print("FROM FORM 3 EDIT RECIPE: ", data )
    # Recipe.update_recipe(data)
    # return redirect('/dashboard')
    print("END OF ADD RECIPE PART++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if Recipe.validate_Update_Recipe(data):
        Recipe.update_recipe(data)
        flash("Updated successfully")
        return redirect('/dashboard')
    else:
        print("invalid values")
    return redirect('/recipes/new')

@app.route("/recipes/delete/<id>")
def deleteThisRecipe(id):
    if 'users_id' not in session:
        return redirect("/")
    Recipe.delete_recipe(id)
    return redirect('/dashboard')


