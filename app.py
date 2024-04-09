#!/usr/bin/python3

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    try:

        data = request.get_json()
        title = data['title']
        cuisine = data['cuisine']
        difficulty = data['difficulty']


        new_recipe = Recipe(title=title, cuisine=cuisine,
                difficulty=difficulty)


        db.session.add(new_recipe)
        db.session.commit()

        return 'Recipe added successfully!'
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':

    app.run(debug=False)
