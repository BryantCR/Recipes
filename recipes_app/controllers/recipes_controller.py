from flask import render_template, request, redirect, session
from recipes_app import app
from recipes_app.models.Recipe import Recipe

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
    #     User.register_login(data)
    # else:
    #     print("invalid values")
    # return redirect('/login')

@app.route("/recipes/delete/<id>")
def deleteRecipe(id):
	data = {
		"users_id" : users_id
    }
    Recipe.delete_recipe(data)
    return redirect("/dashboard")





