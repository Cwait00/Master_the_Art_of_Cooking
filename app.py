#!/usr/bin/python3

# app.py
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    # Add more columns as needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    # Retrieve recipe data from request
    data = request.get_json()
    title = data['title']
    cuisine = data['cuisine']
    difficulty = data['difficulty']

    # Create new recipe object
    new_recipe = Recipe(title=title, cuisine=cuisine, difficulty=difficulty)

    # Add new recipe to the database
    db.session.add(new_recipe)
    db.session.commit()

    return 'Recipe added successfully!'

# Now you can access the configuration settings like this:
print(app.config['DEBUG'])         # Output: True
print(app.config['SECRET_KEY'])    
# Output: '218428b7cb03dd38eb995131a64b4f640a6ec844b6144ea0'
print(app.config['DATABASE_URI'])  
# Output: 'mysql://root:thenjiwe24@172.17.0.15:3306/mysql'
print(app.config['API_KEY'])       # Output: 'your_api_key'

# Add more routes and logic as needed

if __name__ == '__main__':
    app.run()
