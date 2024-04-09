#!/usr/bin/python3

def display_recipe(recipe):
    """Display information about a recipe."""
    print(f"Recipe: {recipe['title']}")
    print(f"Cuisine: {recipe['cuisine']}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print("Instructions:")
    for step in recipe['instructions']:
        print(f"{step}")
    print("Reviews:")
    for review in recipe['reviews']:
        print(f"- {review}")

if __name__ == "__main__":

    recipe = {
        'title': 'Spaghetti Carbonara',
        'cuisine': 'Italian',
        'difficulty': 'Medium',
        'ingredients': ['Spaghetti', 'Eggs', 'Pancetta', 'Parmesan Cheese',
                'Black Pepper'],
        'instructions': [
            'Cook spaghetti according to package instructions.',
            'In a separate bowl, whisk together eggs, cheese, and pepper.',
            'In a pan, cook pancetta until crispy. Drain fat and set aside.',
            'Once spaghetti is cooked, reserve some pasta water and drain.',
            'Add hot spaghetti to egg mixture and toss quickly to coat.
                The heat from the pasta will cook the eggs.',
            'Add pancetta and mix well. If too dry, add reserved
                pasta water to loosen the sauce.',
            'Serve immediately with additional cheese and pepper.'
        ],
        'reviews': [
            'Delicious and easy to make!',
            'Authentic flavor, just like in Italy.',
            'My family loved it!'
        ]
    }

    display_recipe(recipe)
