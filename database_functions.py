import datetime as dt
import sqlite3
from sqlite3 import Error
import lists


def create_connection(db):
    """Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def orders():
    conn = create_connection('orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS orders (date TEXT, number TEXT, time TEXT, server TEXT, tabl TEXT,'
                'guest1 TEXT, guest2 TEXT, guest3 TEXT, guest4 TEXT, guest5 TEXT, guest6 TEXT, guest7 TEXT,'
                'guest8 TEXT, guest9 TEXT, guest10 TEXT, guest11 TEXT, guest12 TEXT, total TEXT)')

    date = dt.datetime.now().strftime("%y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M\n")
    ordernum = str(lists.order_number) + '\n'

    guest1 = ''
    guest2 = ''
    guest3 = ''
    guest4 = ''
    guest5 = ''
    guest6 = ''
    guest7 = ''
    guest8 = ''
    guest9 = ''
    guest10 = ''
    guest11 = ''
    guest12 = ''

    for i in lists.order:
        split_guest = i.split(':')
        guest = split_guest[0]
        order = "{}, ".format(split_guest[1])
        if guest == 'Guest 1':
            guest1 += order
        elif guest == 'Guest 2':
            guest2 += order
        elif guest == 'Guest 3':
            guest3 += order
        elif guest == 'Guest 4':
            guest4 += order
        elif guest == 'Guest 5':
            guest5 += order
        elif guest == 'Guest 6':
            guest6 += order
        elif guest == 'Guest 7':
            guest7 += order
        elif guest == 'Guest 8':
            guest8 += order
        elif guest == 'Guest 9':
            guest9 += order
        elif guest == 'Guest 10':
            guest10 += order
        elif guest == 'Guest 11':
            guest11 += order
        else:
            guest12 += order

    server = lists.server.strip("\n")
    table = lists.table.strip("\n")

    cur.execute("INSERT INTO orders (date, number, time, server, tabl, guest1, guest2, guest3,  guest4,"
                "guest5, guest6, guest7, guest8, guest9, guest10, guest11, guest12, total) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (date, ordernum, time, server, table, guest1, guest2, guest3, guest4, guest5, guest6, guest7, guest8,
                 guest9, guest10, guest11, guest12, lists.total))
    conn.commit()
    conn.close()


def inventory():
    """"Change to select from completed orders. Make sure bar also goes here"""
    date = dt.datetime.now().strftime("%y-%m-%d")
    conn = create_connection('kitchen_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT * FROM kitchen_orders')
    data = cur.fetchall()
    conn.close()

    menu = lists.menu

    inv = {}
    for m in menu:
        inv.update({m: 0})

    for d in data:
        items = d[4].split('\n')
        for i in items:
            i = i.replace(' ', '').replace("'", "").replace(".", "").replace("/", "")
            for n in range(len(inv)):
                if i == menu[n]:
                    inv[menu[n]] += 1

    conn = create_connection('bar_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT * FROM bar_orders')
    data = cur.fetchall()
    conn.close()

    for d in data:
        items = d[4].split('\n')
        for i in items:
            i = i.replace(' ', '').replace("'", "").replace(".", "").replace("/", "")
            for n in range(len(inv)):
                if i == menu[n]:
                    inv[menu[n]] += 1

    conn = create_connection('inventory.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS inventory (date TEXT UNIQUE, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT,'
                '{} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, '
                '{} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT,'
                '{} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT, {} TEXT,'
                '{} TEXT, {} TEXT)'.format(menu[0], menu[1], menu[2], menu[3], menu[4], menu[5], menu[6], menu[7],
                                           menu[8], menu[9], menu[10], menu[11], menu[12], menu[13], menu[14], menu[15],
                                           menu[16], menu[17], menu[18], menu[19], menu[20], menu[21], menu[22],
                                           menu[23], menu[24], menu[25], menu[26], menu[27], menu[28], menu[29],
                                           menu[30], menu[31], menu[32], menu[33], menu[34], menu[35], menu[36],
                                           menu[37], menu[38], menu[39]))
    cur.execute('INSERT OR REPLACE INTO inventory (date,{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'
                '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                .format(menu[0], menu[1], menu[2], menu[3], menu[4], menu[5], menu[6], menu[7], menu[8], menu[9],
                        menu[10], menu[11], menu[12], menu[13], menu[14], menu[15], menu[16], menu[17],  menu[18],
                        menu[19], menu[20], menu[21], menu[22], menu[23], menu[24], menu[25], menu[26], menu[27],
                        menu[28], menu[29], menu[30], menu[31], menu[32], menu[33], menu[34], menu[35], menu[36],
                        menu[37], menu[38], menu[39]),
                (date, inv[lists.menu[0]], inv[menu[1]], inv[menu[2]], inv[menu[3]], inv[menu[4]], inv[menu[5]],
                 inv[menu[6]], inv[menu[7]], inv[menu[8]], inv[menu[9]], inv[menu[10]], inv[menu[11]], inv[menu[12]],
                 inv[menu[13]], inv[menu[14]], inv[menu[15]], inv[menu[16]], inv[menu[17]], inv[menu[18]],
                 inv[menu[19]], inv[menu[20]], inv[menu[21]], inv[menu[22]], inv[menu[23]], inv[menu[24]],
                 inv[menu[25]], inv[menu[26]], inv[menu[27]], inv[menu[28]], inv[menu[29]], inv[menu[30]],
                 inv[menu[31]], inv[menu[32]], inv[menu[33]], inv[menu[34]], inv[menu[35]], inv[menu[36]],
                 inv[menu[37]], inv[menu[38]], inv[menu[39]]))

    conn.commit()
    conn.close()


def kitchen_orders():
    conn = create_connection('kitchen_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS kitchen_orders (number TEXT, time TEXT, server TEXT, tabl TEXT, '
                'items TEXT)')

    time = dt.datetime.now().strftime("%H:%M\n")
    ordernum = str(lists.order_number) + '\n'

    order = ''

    for i in lists.order:
        split_guest = i.split(':')
        remove_guest = split_guest[1]
        split_price = remove_guest.split('$')
        spaced_item = split_price[0]
        item = spaced_item.strip()
        if item in lists.entrees or item in lists.appetizers:
            order += item+' \n'
    if order:
        cur.execute("INSERT INTO kitchen_orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                    (ordernum, time, lists.server, lists.table, order))
    conn.commit()
    conn.close()


def bar_orders():
    conn = create_connection('bar_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS bar_orders (number TEXT, time TEXT, server TEXT, tabl TEXT, '
                'items TEXT)')

    time = dt.datetime.now().strftime("%H:%M\n")
    ordernum = str(lists.order_number) + '\n'

    order = ''

    for i in lists.order:
        split_guest = i.split(':')
        remove_guest = split_guest[1]
        split_price = remove_guest.split('$')
        spaced_item = split_price[0]
        item = spaced_item.strip()
        if item in lists.drinks:
            order += item+' \n'
    if order:
        cur.execute("INSERT INTO bar_orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                    (ordernum, time, lists.server, lists.table, order))
    conn.commit()
    conn.close()


def finished_orders_db(ordernum, time, server, table, food):
    conn = create_connection('finished_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS orders (number TEXT, time TEXT, server TEXT, tabl TEXT, items TEXT)')

    cur.execute("INSERT INTO orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                (ordernum, time, server, table, food))
    conn.commit()


def total_day():
    date = dt.datetime.now().strftime("%y-%m-%d")
    conn = create_connection('orders.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT server, total FROM orders WHERE date=?', (date,))
    data = cur.fetchall()

    conn.close()

    server1 = 0
    server2 = 0
    server3 = 0

    for d in data:
        if d[0] == "Server 1":
            server1 += float(d[1])
        elif d[0] == "Server 2":
            server2 += float(d[1])
        if d[0] == "Server 3":
            server3 += float(d[1])

    conn = create_connection('totals.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS totals (date TEXT UNIQUE, server1 FLOAT, server2 FLOAT, server3 FLOAT)')
    cur.execute('INSERT OR REPLACE INTO totals (date, server1, server2, server3) VALUES (?,?,?,?)',
                (date, server1, server2, server3))

    conn.commit()
    conn.close()
