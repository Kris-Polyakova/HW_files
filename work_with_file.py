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




