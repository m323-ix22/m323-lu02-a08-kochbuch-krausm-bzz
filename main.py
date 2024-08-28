"""
Skript
"""

import json


def adjust_recipe(recipe, amount_people):
    new_ingredients = {}
    ingredients = recipe['ingredients']
    servings = recipe['servings']
    factor = amount_people / servings

    for ingredient, amount in ingredients.items():
        new_ingredients[ingredient] = amount * factor

    new_recipe = {
        'title': recipe['title'],
        'ingredients': new_ingredients,
        'servings': amount_people
    }
    return new_recipe


def load_recipe(json_recipe):
    return json.loads(json_recipe)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = (
        '{"title": "Spaghetti Bolognese", '
        '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, '
        '"servings": 4}'
    )
    original_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(original_recipe, 8)
    print(f'Original Recipe: {original_recipe}')
    print(f'Adjusted Recipe: {adjusted_recipe}')
