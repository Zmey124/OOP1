

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    recipe_name = None
    ingredients = []

    for line in file:
        line = line.strip()

        if line == '':  # Empty line indicates end of recipe
            if recipe_name:
                cook_book[recipe_name] = ingredients
                recipe_name = None
                ingredients = []

        elif recipe_name is None:  # First line of a new recipe
            recipe_name = line
            num_steps = int(file.readline().strip())  # Read the number of steps (ignore it for now)
            file.readline()  # Skip the empty line

        else:  # Ingredient line
            ingredient_name, quantity, unit = line.split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': unit})

# Handle the last recipe (no empty line after it)
if recipe_name:
    cook_book[recipe_name] = ingredients

print(cook_book)