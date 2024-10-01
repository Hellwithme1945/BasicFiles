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

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Блюда '{dish}' нет в книге рецептов.")
    return shop_list

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count)

for ingredient, details in shop_list.items():
    print(f"{ingredient}: {details}")
