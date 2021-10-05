from flask import Flask, render_template, request, redirect, session
from recipes_app import app
from recipes_app.controllers import users_controller

if __name__ == "__main__":
    app.run( debug = True )
