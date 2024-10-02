cart = []


def add_to_cart(item_name, price, quantity=1):
    global cart
    item = {
        'name': item_name,
        'price': price,
        'quantity': quantity
    }
    cart.append(item)
    print(f'Добавлен товар: {item_name}, цена: {price}, количество: {quantity}')


def calculate_total_price(items):
    if not items:
        return 0
    else:
        first_item = items[0]
        return first_item['price'] * first_item['quantity'] + calculate_total_price(items[1:])


def checkout(*items):
    for item in items:
        add_to_cart(*item)


def customer_info(**info):
    print('Информация о покупателе')
    for key, value in info.items():
        print(f'{key}: {value}')


def remove_from_cart(item_name):
    global cart
    item_to_keep = []
    for item in cart:
        if item['name'] != item_name:
            item_to_keep.append(item)
    cart = item_to_keep
    print(f'Товар {item_name} удалён из корзины')


def apply_discount(discount_func):
    global cart
    for item in cart:
        original_price = item['price']
        item['price'] = discount_func(item['price'])
        print(f'На товар {item['name']} применена скидка. Цена: {original_price} -> {item['price']}')


def ten_percent_discount(price):
    return price * 0.9


def count_item_in_cart(item_name, items):
    if not items:
        return 0
    elif items[0]['name'] == item_name:
        return items[0]['quantity'] + count_item_in_cart(item_name, items[1:])
    else:
        return count_item_in_cart(item_name, items[1:])


def show_cart():
    if not cart:
        print('Корзина пуста')
    else:
        print('Тукущие товары в корзине')
        for item in cart:
            print(f'{item['name']}: {item['quantity']} штук. Цена: {item['price']}')



add_to_cart('Книга', 1000)
add_to_cart('Ноутбук', 200000, 2)

total = calculate_total_price(cart)
print(f'Итоговая сумма в корзине: {total}')

checkout(('Телефон', 30000, 2), ('Планшет', 60000, 6))

customer_info(name='Артём', age=44, city='Москва', email='artem@mail.ru')

remove_from_cart('Ноутбук')

apply_discount(ten_percent_discount)

count = count_item_in_cart('Планшет', cart)
print(f'Количество {count}')

show_cart()
