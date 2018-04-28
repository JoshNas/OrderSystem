import lists


def clear_lists():
    lists.order = []
    lists.total = 0
    lists.server = ''
    lists.table = ''
    lists.current_guest = ''
    lists.server_set = False
    lists.table_set = False
    lists.guest_set = False


def get_food(order):
    split_guest = order.split(':')
    remove_guest = split_guest[1]
    split_price = remove_guest.split('$')
    spaced_item = split_price[0]
    item = spaced_item.strip()
    if item in lists.entrees:
        return item


def get_appetizers():
    with open("appetizers.csv") as menu:
        for row in menu:
            entry = row.split(',')
            price = entry[1].strip('\n')
            lists.appetizers.append(entry[0])
            lists.appetizers_prices.append(int(price))


def get_entrees():
    with open('entrees.csv') as menu:
        for row in menu:
            entry = row.split(',')
            price = entry[1].strip('\n')
            lists.entrees.append(entry[0])
            lists.entrees_prices.append(int(price))


def get_bar_menu():
    with open('barmenu.csv') as menu:
        for row in menu:
            entry = row.split(',')
            price = entry[1].strip('\n')
            lists.drinks.append(entry[0])
            lists.drinks_prices.append(int(price))


def get_row_nums():
    with open('perRow.csv') as rows:
        for row in rows:
            entry = row.split(',')
            item = entry[0]
            num = entry[1].strip('\n').strip(' ')
            lists.per_row[item] = num

