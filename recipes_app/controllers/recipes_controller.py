from flask import render_template, request, redirect, session
from recipes_app import app
from recipes_app.models.Recipe import Recipe
from recipes_app.models.User import User

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
    Recipe.add_new_recipe(data)
    return redirect('/dashboard')
    print("END OF ADD RECIPE PART++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # if User.validate_registration(data):
    #     User.add_new_recipe(data)
    # else:
    #     print("invalid values")
    # return redirect('/login')

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

@app.route("/recipes/delete/<id>")
def deleteThisRecipe(id):
    data={
        'id': id
    }
    result2 = Recipe.delete_recipe(data)
    print("DELETE: ", result2)
    return redirect('/dashboard')


