with open ('recipes.txt', 'r', encoding = 'utf-8') as f:
    cook_book = {}
    counter = 0
    dish = ''
    for line in f:
        counter += 1
        if line == '\n':
            counter = 0
        if counter == 1:
            dish = line.strip()
            cook_book[dish] = []
        if counter > 2:
            splitted_line = line.strip().split(' | ')
            ingredients = {}
            ingredients['ingredient_name'] = splitted_line[0]
            ingredients['quantity'] = int(splitted_line[1])
            ingredients['measure'] = splitted_line[2]
            cook_book[dish].append(ingredients)
            
dishes = ['Омлет', 'Омлет с беконом', 'Запеченный картофель', 'Десерт с вишней']

def get_buy_list_by_dishes(dishes = list, person_count = int):
    shopping_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for product in cook_book[dish]:
                product_key = product['ingredient_name']
                product_value = {}
                if product_key in shopping_dict:
                    old_value = shopping_dict[product_key].get('quantity')
                    new_value = product.get('quantity') * person_count
                    product_value['quantity'] = int(old_value + new_value)
                else:
                    shopping_dict[product_key] = {}
                    product_value['measure'] = product.get('measure')
                    product_value['quantity'] = product.get('quantity') * person_count
                shopping_dict[product_key].update(product_value)
    return shopping_dict
   
print(get_buy_list_by_dishes(dishes,1))
