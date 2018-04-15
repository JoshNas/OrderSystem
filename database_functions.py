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
    conn = create_connection('complete_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS complete_orders (date TEXT, number TEXT, time TEXT, server TEXT, tabl TEXT,'
                'guest1 TEXT, guest2 TEXT, guest3 TEXT, total TEXT)')

    date = dt.datetime.now().strftime("%y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M\n")
    ordernum = str(lists.order_number) + '\n'

    guest1 = ''
    guest2 = ''
    guest3 = ''
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

        order = order.split('$')
        order = order[0].strip(' ')
        """Add this to inventory db"""
        print(order)

    server = lists.server.strip("\n")
    table = lists.table.strip("\n")

    cur.execute("INSERT INTO complete_orders (date, number, time, server, tabl, guest1, guest2, guest3, total) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (date, ordernum, time, server, table, guest1, guest2, guest3, lists.total))
    conn.commit()


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

    cur.execute("INSERT INTO kitchen_orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                (ordernum, time, lists.server, lists.table, order))
    conn.commit()


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

    cur.execute("INSERT INTO bar_orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                (ordernum, time, lists.server, lists.table, order))
    conn.commit()






def finished_orders_db(ordernum, time, server, table, food):
    conn = create_connection('finished_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS orders (number TEXT, time TEXT, server TEXT, tabl TEXT, items TEXT)')

    cur.execute("INSERT INTO orders (number, time, server, tabl, items) VALUES (?, ?, ?, ?, ?)",
                (ordernum, time, server, table, food))
    conn.commit()


def total_day():
    date = dt.datetime.now().strftime("%y-%m-%d")
    conn = create_connection('complete_orders.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT server, total FROM complete_orders WHERE date=?', (date,))
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
















































