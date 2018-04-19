import tkinter as tk
import database_functions as dbf
import datetime as dt
import csv


class ManagerApplication(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1080x760')
        self.root.title("Manager")

        self.message = tk.Text(self.root, height=1, width=80)
        self.message.grid(row=0, column=0, sticky='new')

        self.keypad = tk.Canvas()
        self.keypad.grid(row=1, column=0, sticky='nsew')

        self.order_window = tk.Canvas()
        self.order_window.grid(row=0, column=2, sticky='nsew')

        self.display_window = tk.Text(self.order_window, height=35, width=80)
        self.display_window.grid(row=0, column=0, columnspan=12)

        """Buttons"""
        tk.Button(self.keypad, text='Total Day', command=self.manager_total_day).grid(row=0, column=0, sticky='nsew')
        # tk.Button(self.keypad, text='Total Bar', command=self.total_bar).grid(row=0, column=1, sticky='nsew')
        #
        # tk.Button(self.keypad, text='Server 1', command=self.total_server1).grid(row=1, column=0, sticky='nsew')
        # tk.Button(self.keypad, text='Server 2', command=self.total_server2).grid(row=1, column=1, sticky='nsew')
        # tk.Button(self.keypad, text='Server 3', command=self.total_server3).grid(row=1, column=2, sticky='nsew')
        # tk.Button(self.keypad, text='Server 4', command=self.total_server4).grid(row=1, column=3, sticky='nsew')
        # tk.Button(self.keypad, text='Server 5', command=self.total_server5).grid(row=1, column=4, sticky='nsew')
        # tk.Button(self.keypad, text='Server 6', command=self.total_server6).grid(row=1, column=5, sticky='nsew')
        #
        # tk.Button(self.keypad, text='Add to entrees', command=self.add_to_entrees).grid(row=2, column=1, sticky='nsew')
        # tk.Button(self.keypad, text='Add to appetizers', command=self.add_to_appetizers).grid(row=2, column=2, sticky='nsew')
        # tk.Button(self.keypad, text='Add to desserts', command=self.add_to_desserts).grid(row=2, column=3, sticky='nsew')
        # tk.Button(self.keypad, text='Add to bar', command=self.add_to_bar).grid(row=2, column=4, sticky='nsew')

    tip_out_percent = .08

    def manager_total_day(self):
        dbf.total_day()
        conn = dbf.create_connection('totals.sqlite3')
        cur = conn.cursor()
        date = dt.datetime.now().strftime("%y-%m-%d")
        cur.execute('SELECT * FROM totals WHERE date=?', (date,))

        rows = cur.fetchall()

        server1_total = 0
        server2_total = 0
        server3_total = 0

        server1_tipout = server1_total * self.tip_out_percent
        server2_tipout = server2_total * self.tip_out_percent
        server3_tipout = server3_total * self.tip_out_percent

        for row in rows:
            server1_total += row[1]
            server2_total += row[2]
            server3_total += row[3]

        total = server1_total + server2_total + server3_total

        self.display_window.delete(1.0, 'end')
        self.display_window.insert('end', '          TOTAL      TIP OUT'.format(server1_total, server1_tipout))
        self.display_window.insert('end', '\nServer 1: ${}     ${}'.format(server1_total, server1_tipout))
        self.display_window.insert('end', '\nServer 2: ${}     ${}'.format(server2_total, server2_tipout))
        self.display_window.insert('end', '\nServer 3: ${}     ${}'.format(server3_total, server3_tipout))
        self.display_window.insert('end', '\nTotal:    ${}'.format(total))

        conn.close()


def update_menu(menu, item, price):
    # conn = dbf.create_connection('inventory.sqlite3')
    # cur = conn.cursor()
    # cur.execute("ALTER TABLE inventory ADD COLUMN {}".format(item.replace(' ', '')))
    # conn.commit()
    # conn.close()

    addition = '\n{}, {}'.format(item, price)
    file = '{}.csv'.format(menu)
    with open(file, 'a') as f:
        f.write(addition)



update_menu('barmenu', 'Jack Daniels', '5')

































if __name__ == "__main__":
    myApp = ManagerApplication()
    myApp.root.mainloop()