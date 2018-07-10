import tkinter as tk
import database_functions as dbf
import datetime as dt
import os


class ManagerApplication(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1080x760')
        self.root.title("Manager")

        self.entry_window = tk.Canvas(self.root)
        self.entry_window.grid(row=0, column=0)
        tk.Label(self.entry_window, text='Item').grid(row=0, column=0, sticky='nsew')
        tk.Label(self.entry_window, text='Price').grid(row=0, column=1, sticky='nsew')
        tk.Label(self.entry_window, text='Menu').grid(row=0, column=2, sticky='nsew')

        self.item_entry = tk.Entry(self.entry_window, width=40)
        self.item_entry.grid(row=1, column=0, sticky='nsew')
        self.price_entry = tk.Entry(self.entry_window, width=10)
        self.price_entry.grid(row=1, column=1, sticky='nsew')

        self.menus = tk.StringVar(self.root)  # Create a Tkinter variable
        choices = {'test.csv', 'entrees.csv', 'appetizers.csv', 'barmenu.csv'}  # Dictionary with options
        self.menus.set('test.csv')  # set the default option
        self.menu_selector = tk.OptionMenu(self.entry_window, self.menus, *choices).grid(row=1, column=2, sticky='new')

        self.selector_window = tk.Canvas(self.root)  # Selector Window
        self.selector_window.grid(row=2, column=0)
        tk.Label(self.selector_window, text='Apps').grid(row=0, column=0)
        tk.Label(self.selector_window, text='Entrees').grid(row=0, column=1)
        tk.Label(self.selector_window, text='Drinks').grid(row=0, column=2)
        tk.Label(self.selector_window, text='per Row').grid(row=0, column=3)

        self.appnum = tk.StringVar(self.root)
        appnums = {3, 4, 5}
        self.appnum.set(3)
        self.app_selector = tk.OptionMenu(self.selector_window, self.appnum, *appnums).grid(row=1, column=0)

        self.entreenum = tk.StringVar(self.root)
        entreenums = {4, 5}
        self.entreenum.set(4)
        self.entree_selector = tk.OptionMenu(self.selector_window, self.entreenum, *entreenums)\
            .grid(row=1, column=1)

        self.drinknum = tk.StringVar(self.root)
        drinknums = {4, 5}
        self.drinknum.set(4)
        self.drink_selector = tk.OptionMenu(self.selector_window, self.drinknum, *drinknums)\
            .grid(row=1, column=2)

        # keypad for buttons to total
        self.keypad = tk.Canvas()
        self.keypad.grid(row=1, column=0, sticky='nsew')

        tk.Label(self.keypad, text='Month').grid(row=1, column=3, sticky='nsew')
        self.month = tk.StringVar(self.root)
        months = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
        self.month.set(1)  # set the default option
        self.month_selector = tk.OptionMenu(self.keypad, self.month, *months).grid(row=2, column=3, sticky='new')

        tk.Label(self.keypad, text='Day').grid(row=1, column=4, sticky='nsew')
        self.day = tk.StringVar(self.root)
        days = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31}
        self.day.set(1)
        self.day_selector = tk.OptionMenu(self.keypad, self.day, *days).grid(row=2, column=4, sticky='new')

        tk.Label(self.keypad, text='Year').grid(row=1, column=5, sticky='nsew')
        self.year = tk.StringVar(self.root)
        years = {18, 19, 20}
        self.year.set(18)
        self.year_selector = tk.OptionMenu(self.keypad, self.year, *years).grid(row=2, column=5, sticky='new')

        tk.Label(self.keypad, text='Month').grid(row=3, column=3, sticky='nsew')
        self.month2 = tk.StringVar(self.root)
        self.month2.set(1)  # set the default option
        self.month_selector = tk.OptionMenu(self.keypad, self.month2, *months).grid(row=4, column=3, sticky='new')

        tk.Label(self.keypad, text='Day').grid(row=3, column=4, sticky='nsew')
        self.day2 = tk.StringVar(self.root)
        self.day2.set(1)
        self.day_selector = tk.OptionMenu(self.keypad, self.day2, *days).grid(row=4, column=4, sticky='new')

        tk.Label(self.keypad, text='Year').grid(row=3, column=5, sticky='nsew')
        self.year2 = tk.StringVar(self.root)
        self.year2.set(18)
        self.year_selector = tk.OptionMenu(self.keypad, self.year2, *years).grid(row=4, column=5, sticky='new')

        tk.Label(self.keypad, text='Tip Out %').grid(row=5, column=0, sticky='nsew')
        self.tipout = tk.StringVar(self.root)
        tipout_percent = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        self.tipout.set(8)
        self.year_selector = tk.OptionMenu(self.keypad, self.tipout, *tipout_percent).grid(row=6, column=0, sticky='new')

        self.display_window = tk.Canvas()
        self.display_window.grid(row=1, column=1, sticky='nsew')

        self.dis_window = tk.Text(self.display_window, height=25, width=40)
        self.dis_window.grid(row=1, column=0)

        """Buttons"""
        tk.Button(self.keypad, text='Update Menu', command=self.update_menu).grid(row=0, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Display Menu', command=self.display_menu).grid(row=0, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Delete Item', command=self.delete_from_menu).grid(row=0, column=2, sticky='nsew')
        tk.Button(self.selector_window, text='Set', command=self.set_num_per_rows).grid(row=1, column=3, sticky='nsew')
        tk.Button(self.keypad, text='Totals', command=self.get_totals).grid(row=2, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Total Day', command=self.manager_total_day).grid(row=2, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Total Date', command=self.date_totals).grid(row=2, column=2, sticky='nsew')
        tk.Button(self.keypad, text='Date Range', command=self.date_range_totals).grid(row=4, column=2, sticky='nsew')

    def get_totals(self):
        conn = dbf.create_connection('totals.sqlite3')
        cur = conn.cursor()
        cur.execute('SELECT * FROM totals')
        rows = cur.fetchall()

        server1_total = 0
        server2_total = 0
        server3_total = 0

        for row in rows:
            server1_total += row[1]
            server2_total += row[2]
            server3_total += row[3]

        total = server1_total + server2_total + server3_total

        self.dis_window.delete(1.0, 'end')
        self.dis_window.insert('end', '          TOTAL'.format(server1_total))
        self.dis_window.insert('end', '\nServer 1: ${}'.format(server1_total))
        self.dis_window.insert('end', '\nServer 2: ${}'.format(server2_total))
        self.dis_window.insert('end', '\nServer 3: ${}'.format(server3_total))
        self.dis_window.insert('end', '\nTotal:    ${}'.format(total))

        conn.close()

    def date_totals(self):
        month = self.month.get()
        if len(month) < 2:
            month = '0{}'.format(month)
        day = self.day.get()
        if len(day) < 2:
            day = '0{}'.format(day)
        year = self.year.get()
        date = '{}-{}-{}'.format(year, month, day)

        conn = dbf.create_connection('totals.sqlite3')
        cur = conn.cursor()
        cur.execute('SELECT * FROM totals WHERE date=?', (date,))
        rows = cur.fetchall()

        server1_total = 0
        server2_total = 0
        server3_total = 0

        for row in rows:
            server1_total += row[1]
            server2_total += row[2]
            server3_total += row[3]

        total = server1_total + server2_total + server3_total

        self.dis_window.delete(1.0, 'end')
        self.dis_window.insert('end', '          TOTAL'.format(server1_total))
        self.dis_window.insert('end', '\nServer 1: ${}'.format(server1_total))
        self.dis_window.insert('end', '\nServer 2: ${}'.format(server2_total))
        self.dis_window.insert('end', '\nServer 3: ${}'.format(server3_total))
        self.dis_window.insert('end', '\nTotal:    ${}'.format(total))

        conn.close()

    def date_range_totals(self):
        month = self.month.get()
        if len(month) < 2:
            month = '0{}'.format(month)
        day = self.day.get()
        if len(day) < 2:
            day = '0{}'.format(day)
        year = self.year.get()
        date = '{}-{}-{}'.format(year, month, day)

        month2 = self.month2.get()
        if len(month2) < 2:
            month2 = '0{}'.format(month2)
        day2 = self.day2.get()
        if len(day2) < 2:
            day2 = '0{}'.format(day2)
        year2 = self.year2.get()
        date2 = '{}-{}-{}'.format(year2, month2, day2)

        conn = dbf.create_connection('totals.sqlite3')
        cur = conn.cursor()
        cur.execute('SELECT * FROM totals WHERE date BETWEEN ? AND ?', (date, date2))
        rows = cur.fetchall()

        server1_total = 0
        server2_total = 0
        server3_total = 0

        for row in rows:
            server1_total += row[1]
            server2_total += row[2]
            server3_total += row[3]

        total = server1_total + server2_total + server3_total

        self.dis_window.delete(1.0, 'end')
        self.dis_window.insert('end', '          TOTAL'.format(server1_total))
        self.dis_window.insert('end', '\nServer 1: ${}'.format(server1_total))
        self.dis_window.insert('end', '\nServer 2: ${}'.format(server2_total))
        self.dis_window.insert('end', '\nServer 3: ${}'.format(server3_total))
        self.dis_window.insert('end', '\nTotal:    ${}'.format(total))

        conn.close()

    def manager_total_day(self):
        dbf.total_day()
        conn = dbf.create_connection('totals.sqlite3')
        cur = conn.cursor()
        date = dt.datetime.now().strftime("%y-%m-%d")
        cur.execute('SELECT * FROM totals WHERE date=?', (date,))

        rows = cur.fetchall()

        tipout = int(self.tipout.get())

        server1_total = 0
        server2_total = 0
        server3_total = 0

        for row in rows:
            server1_total += row[1]
            server2_total += row[2]
            server3_total += row[3]

        server1_tipout = server1_total * (tipout / 100)
        server2_tipout = server2_total * (tipout / 100)
        server3_tipout = server3_total * (tipout / 100)

        total = server1_total + server2_total + server3_total

        self.dis_window.delete(1.0, 'end')
        self.dis_window.insert('end', '          SALES      TIP OUT'.format(server1_total, server1_tipout))
        self.dis_window.insert('end', '\nServer 1: ${}     ${}'.format(server1_total, server1_tipout))
        self.dis_window.insert('end', '\nServer 2: ${}     ${}'.format(server2_total, server2_tipout))
        self.dis_window.insert('end', '\nServer 3: ${}     ${}'.format(server3_total, server3_tipout))
        self.dis_window.insert('end', '\nTotal:    ${}'.format(total))

        conn.close()

    def update_menu(self):
        addition = ''

        if len(self.item_entry.get()) > 0 and len(self.price_entry.get()):
            item = self.item_entry.get()
            price = self.price_entry.get()
            if '$' in price:
                price = price.replace('$', '')
            addition = '{}, {}'.format(item, price)

        menu = self.menus.get()
        self.item_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')

        # do something to make sure addition is formatted correctly
        if os.stat(menu).st_size == 0:
            with open(menu, 'a') as f:
                f.write(addition)
        else:
            with open(menu, 'a') as f:
                addition = '\n{}'.format(addition)
                f.write(addition)

    def delete_from_menu(self):
        selections = self.dis_window.selection_get()
        items = selections.split('\n')
        menu = self.menus.get()
        new_menu = []

        with open(menu, 'r') as m:
            m.seek(0)
            for row in m:
                r = row.strip('\n')
                if r not in items:
                    new_menu.append(r)

        with open(menu, 'w') as m:
            first = True
            for i in new_menu:
                if first:
                    m.write(i)
                    first = False
                else:
                    m.write('\n{}'.format(i))

    def display_menu(self):
        self.dis_window.delete(1.0, 'end')
        menu = self.menus.get()
        with open(menu) as m:
            for row in m:
                self.dis_window.insert('end', row)

    def set_num_per_rows(self):
        with open('perRow.csv', 'w') as f:
            f.write('AppsPerRow, {}'.format(self.appnum.get()))
            f.write('\nEntreesPerRow, {}'.format(self.entreenum.get()))
            f.write('\nDrinksPerRow, {}'.format(self.drinknum.get()))






































if __name__ == "__main__":
    myApp = ManagerApplication()
    myApp.root.mainloop()