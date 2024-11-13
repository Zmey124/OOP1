

cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as file:
    recipe_name = None
    ingredients = []

    for line in file:
        line = line.strip()

        if line == '': 
            if recipe_name:
                cook_book[recipe_name] = ingredients
                recipe_name = None
                ingredients = []

        elif recipe_name is None: 
            recipe_name = line
            num_steps = int(file.readline().strip()) 
            file.readline() 

        else: 
            ingredient_name, quantity, unit = line.split(' | ')
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': unit})

if recipe_name:
    cook_book[recipe_name] = ingredients

print(cook_book)