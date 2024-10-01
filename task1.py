cook_book = {}

with open('C:\\Users\\firer\\Downloads\\recipes.txt', 'r', encoding='utf-8') as file:
    while True:
        dish_name = file.readline().strip()
        if not dish_name:
            break
        ingredient_count = int(file.readline())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_line = file.readline().strip()
            ingredient_name, quantity, measure = [x.strip() for x in ingredient_line.split('|')]
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        cook_book[dish_name] = ingredients
        file.readline()

print(cook_book)
