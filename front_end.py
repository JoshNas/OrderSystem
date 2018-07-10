import tkinter as tk
import lists
import functions as f
import database_functions as dbf


class ServerApplication(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1080x760')
        self.root.title("Your Resturants Name")

        self.message = tk.Text(self.root, height=1, width=80)
        self.message.grid(row=0, column=0)

        self.keypad = tk.Canvas()
        self.keypad.grid(row=1, column=0, sticky='nsew')

        self.order_window = tk.Canvas()
        self.order_window.grid(row=1, column=2, sticky='nsew')

        self.table_window = tk.Text(self.order_window, height=3, width=80)
        self.table_window.grid(row=0, column=2, sticky='nsew')

        self.item_window = tk.Text(self.order_window, height=35, width=80)
        self.item_window.grid(row=1, column=0, columnspan=12)

        self.price_window = tk.Text(self.order_window, height=4, width=80)
        self.price_window.grid(row=2, column=0, columnspan=12)

        """Buttons"""






        tk.Button(self.keypad, text='Server1', command=self.set_server1).grid(row=1, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Server2', command=self.set_server2).grid(row=2, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Server3', command=self.set_server3).grid(row=3, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Server4', command=self.set_server4).grid(row=4, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Server5', command=self.set_server5).grid(row=5, column=0, sticky='nsew')
        tk.Button(self.keypad, text='Server6', command=self.set_server6).grid(row=6, column=0, sticky='nsew')

        tk.Button(self.keypad, text='Table 1', command=self.set_table1).grid(row=1, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 2', command=self.set_table2).grid(row=2, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 3', command=self.set_table3).grid(row=3, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 4', command=self.set_table4).grid(row=4, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 5', command=self.set_table5).grid(row=5, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 6', command=self.set_table6).grid(row=6, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 7', command=self.set_table7).grid(row=7, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 8', command=self.set_table8).grid(row=8, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 9', command=self.set_table9).grid(row=9, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 10', command=self.set_table10).grid(row=10, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 11', command=self.set_table11).grid(row=11, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 12', command=self.set_table12).grid(row=12, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 13', command=self.set_table13).grid(row=13, column=1, sticky='nsew')
        tk.Button(self.keypad, text='Table 14', command=self.set_table14).grid(row=14, column=1, sticky='nsew')

        tk.Button(self.keypad, text='Guest 1', command=self.set_guest1).grid(row=1, column=2, sticky='nsew')
        tk.Button(self.keypad, text='Guest 2', command=self.set_guest2).grid(row=2, column=2, sticky='nsew')
        tk.Button(self.keypad, text='Guest 3', command=self.set_guest3).grid(row=3, column=2, sticky='nsew')

        appetizer_functions = [self.app1, self.app2, self.app3, self.app4, self.app5, self.app6, self.app7, self.app8,
                               self.app9, self.app10]

        entree_functions = [self.item1, self.item2, self.item3, self.item4, self.item5, self.item6, self.item7,
                            self.item8, self.item9, self.item10, self.item11, self.item12, self.item13, self.item14,
                            self.item15, self.item16, self.item17, self.item18, self.item19, self.item20, self.item21,
                            self.item22, self.item23, self.item24, self.item25, self.item26, self.item27, self.item28,
                            self.item29, self.item30, self.item31, self.item32]

        bar_functions = [self.bar_item1, self.bar_item2, self.bar_item3, self.bar_item4, self.bar_item5, self.bar_item6,
                         self.bar_item7, self.bar_item8]

        appetizer_buttons = []
        entree_buttons = []
        drink_buttons = []
        """"Create entree buttons"""
        for i in range(len(lists.appetizers)):
            appetizer_buttons.append(tk.Button(self.keypad, text=lists.appetizers[i], command=appetizer_functions[i],
                                               bg='purple1'))
        for i in range(len(lists.entrees)):
            entree_buttons.append(tk.Button(self.keypad, text=lists.entrees[i], command=entree_functions[i],
                                            bg='royal blue'))
        """Create drink buttons"""
        for i in range(len(lists.drinks)):
            drink_buttons.append(tk.Button(self.keypad, text=lists.drinks[i], command=bar_functions[i],
                                           bg='goldenrod1'))

        """Adds appetizers buttons to GUI"""
        if lists.per_row['AppsPerRow'] == '3':
            for i in range(len(lists.appetizers)):
                if i <= 2:
                    appetizer_buttons[i].grid(row=1, column=3 + i, sticky='nsew')
                elif i <= 5:
                    appetizer_buttons[i].grid(row=2, column=3 + (i - 3), sticky='nsew')
                else:
                    print('Too many items')

        elif lists.per_row['AppsPerRow'] == '4':
            for i in range(len(lists.appetizers)):
                if i <= 3:
                    appetizer_buttons[i].grid(row=1, column=3 + i, sticky='nsew')
                elif i <= 7:
                    appetizer_buttons[i].grid(row=2, column=3 + (i - 4), sticky='nsew')
                else:
                    print('Too many items')

        else:
            for i in range(len(lists.appetizers)):
                if i <= 4:
                    appetizer_buttons[i].grid(row=1, column=3+i, sticky='nsew')
                elif i <= 9:
                    appetizer_buttons[i].grid(row=2, column=3+(i-5), sticky='nsew')
                else:
                    print('Too many items')

        """Adds entree buttons to GUI"""
        if lists.per_row['EntreesPerRow'] == '4':
            for i in range(len(lists.entrees)):
                if i <= 3:
                    entree_buttons[i].grid(row=3, column=3 + i, sticky='nsew')
                elif i <= 7:
                    entree_buttons[i].grid(row=4, column=3 + (i - 4), sticky='nsew')
                elif i <= 11:
                    entree_buttons[i].grid(row=5, column=3 + (i - 8), sticky='nsew')
                elif i <= 15:
                    entree_buttons[i].grid(row=6, column=3 + (i - 12), sticky='nsew')
                elif i <= 19:
                    entree_buttons[i].grid(row=7, column=3 + (i - 16), sticky='nsew')
                elif i <= 23:
                    entree_buttons[i].grid(row=8, column=3 + (i - 20), sticky='nsew')
                elif i <= 27:
                    entree_buttons[i].grid(row=9, column=3 + (i - 24), sticky='nsew')
                elif i <= 31:
                    entree_buttons[i].grid(row=10, column=3 + (i - 28), sticky='nsew')
                else:
                    print('Too many items')
        else:
            for i in range(len(lists.entrees)):
                if i <= 4:
                    entree_buttons[i].grid(row=3, column=3+i, sticky='nsew')
                elif i <= 9:
                    entree_buttons[i].grid(row=4, column=3+(i-5), sticky='nsew')
                elif i <= 14:
                    entree_buttons[i].grid(row=5, column=3+(i-10), sticky='nsew')
                elif i <= 19:
                    entree_buttons[i].grid(row=6, column=3+(i-15), sticky='nsew')
                elif i <= 24:
                    entree_buttons[i].grid(row=7, column=3+(i-20), sticky='nsew')
                elif i <= 29:
                    entree_buttons[i].grid(row=8, column=3+(i-25), sticky='nsew')
                elif i <= 34:
                    entree_buttons[i].grid(row=9, column=3+(i-30), sticky='nsew')
                elif i <= 39:
                    entree_buttons[i].grid(row=10, column=3+(i-35), sticky='nsew')
                else:
                    print('Too many items')

        """"Add drinks"""
        if lists.per_row['DrinksPerRow'] == '4':
            for i in range(len(lists.drinks)):
                if i <= 3:
                    drink_buttons[i].grid(row=12, column=3 + i, sticky='nsew')
                elif i <= 8:
                    drink_buttons[i].grid(row=13, column=3 + (i - 4), sticky='nsew')
                else:
                    print('Too many items')
        else:
            for i in range(len(lists.drinks)):
                if i <= 4:
                    drink_buttons[i].grid(row=12, column=3+i, sticky='nsew')
                elif i <= 9:
                    drink_buttons[i].grid(row=13, column=3+(i-5), sticky='nsew')
                else:
                    print('Too many items')

        remove_last = tk.Button(self.keypad, text='Remove Last', command=self.remove_last_item)
        remove_last.grid(row=15, column=4, sticky='nsew')
        send = tk.Button(self.keypad, text='Send', command=self.send)
        send.grid(row=15, column=6, sticky='nsew')

    # Action buttons
    def clear_windows(self):
        self.table_window.delete(1.0, 'end')
        self.item_window.delete(1.0, 'end')
        self.price_window.delete(1.0, 'end')

    def add_to_order(self, item, price):
        """Checks is server and table are set. If adds item to order."""
        if lists.server_set and lists.table_set and lists.guest_set:
            self.message.delete(1.0, 'end')
            order = '{}: {}  ${}\n'.format(lists.current_guest, item, price)
            lists.order.append(order)
            lists.total += price
            self.display_order()
        else:
            self.table_window.delete(1.0, 'end')
            self.table_window.insert('end', 'Please select Server/Table/Guest')

    def display_table_info(self):
        self.table_window.delete(1.0, 'end')
        self.table_window.insert('end', lists.server)
        self.table_window.insert('end', lists.table)
        self.table_window.insert('end', lists.current_guest)

    def display_order(self):
        self.item_window.delete(1.0, 'end')
        for item in lists.order:
            self.item_window.insert('end', item)
        self.total()

    def total(self):
        pretax_total = lists.total
        tax = lists.total * .08
        total = pretax_total + tax

        pre_tax_total = 'pre-tax: ${:0.2f}\n'.format(pretax_total)
        tax = 'tax: ${:0.2f}\n'.format(tax)
        total = 'total: ${:0.2f}\n'.format(total)
        self.price_window.delete(1.0, 'end')
        self.price_window.insert('end', pre_tax_total)
        self.price_window.insert('end', tax)
        self.price_window.insert('end', total)

    def remove_last_item(self):
        if len(lists.order) > 0:
            last = lists.order.pop()
            split_last = last.split('$')
            price = split_last[1]
            lists.total -= int(price)
            self.display_order()
        else:
            self.message.delete(1.0, 'end')
            self.message.insert('end', 'Order is empty')

    def send(self):
        dbf.orders()
        dbf.kitchen_orders()
        dbf.bar_orders()
        dbf.inventory()
        lists.order_number += 1
        f.clear_lists()
        self.clear_windows()

    # Sets tables
    def set_table1(self):
        self.set_table(1)

    def set_table2(self):
        self.set_table(2)

    def set_table3(self):
        self.set_table(3)

    def set_table4(self):
        self.set_table(4)

    def set_table5(self):
        self.set_table(5)

    def set_table6(self):
        self.set_table(6)

    def set_table7(self):
        self.set_table(7)

    def set_table8(self):
        self.set_table(8)

    def set_table9(self):
        self.set_table(9)

    def set_table10(self):
        self.set_table(10)

    def set_table11(self):
        self.set_table(11)

    def set_table12(self):
        self.set_table(12)

    def set_table13(self):
        self.set_table(13)

    def set_table14(self):
        self.set_table(14)

    # Sets server
    def set_server1(self):
        self.set_server(1)

    def set_server2(self):
        self.set_server(2)

    def set_server3(self):
        self.set_server(3)

    def set_server4(self):
        self.set_server(4)

    def set_server5(self):
        self.set_server(5)

    def set_server6(self):
        self.set_server(6)

    # Sets guest
    def set_guest1(self):
        self.set_guest(1)

    def set_guest2(self):
        self.set_guest(2)

    def set_guest3(self):
        self.set_guest(3)

    def set_server(self, server_number):
        """Sets server based on button selected and displays in GUI"""
        lists.server = ('Server ' + str(server_number) + '\n')
        lists.server_set = True
        self.table_window.delete(1.0, 'end')
        self.display_table_info()

    def set_table(self, table_number):
        """Sets table based on button selected and displays in GUI"""
        lists.table = ('Table ' + str(table_number) + '\n')
        lists.table_set = True
        self.table_window.delete(1.0, 'end')
        self.display_table_info()

    def set_guest(self, guest_number):
        """Sets guest based on button selected and displays in GUI"""
        lists.current_guest = ('Guest ' + str(guest_number))
        lists.guest_set = True
        self.table_window.delete(1.0, 'end')
        self.display_table_info()

    # Appetizers items
    def app1(self):
        item = lists.appetizers[0]
        price = lists.appetizers_prices[0]
        self.add_to_order(item, price)

    def app2(self):
        item = lists.appetizers[1]
        price = lists.appetizers_prices[1]
        self.add_to_order(item, price)

    def app3(self):
        item = lists.appetizers[2]
        price = lists.appetizers_prices[2]
        self.add_to_order(item, price)

    def app4(self):
        item = lists.appetizers[3]
        price = lists.appetizers_prices[3]
        self.add_to_order(item, price)

    def app5(self):
        item = lists.appetizers[4]
        price = lists.appetizers_prices[4]
        self.add_to_order(item, price)

    def app6(self):
        item = lists.appetizers[5]
        price = lists.appetizers_prices[5]
        self.add_to_order(item, price)

    def app7(self):
        item = lists.appetizers[6]
        price = lists.appetizers_prices[6]
        self.add_to_order(item, price)

    def app8(self):
        item = lists.appetizers[7]
        price = lists.appetizers_prices[7]
        self.add_to_order(item, price)

    def app9(self):
        item = lists.appetizers[8]
        price = lists.appetizers_prices[8]
        self.add_to_order(item, price)

    def app10(self):
        item = lists.appetizers[9]
        price = lists.appetizers_prices[9]
        self.add_to_order(item, price)

    # Food items
    def item1(self):
        item = lists.entrees[0]
        price = lists.entrees_prices[0]
        self.add_to_order(item, price)

    def item2(self):
        item = lists.entrees[1]
        price = lists.entrees_prices[1]
        self.add_to_order(item, price)

    def item3(self):
        item = lists.entrees[2]
        price = lists.entrees_prices[2]
        self.add_to_order(item, price)

    def item4(self):
        item = lists.entrees[3]
        price = lists.entrees_prices[3]
        self.add_to_order(item, price)

    def item5(self):
        item = lists.entrees[4]
        price = lists.entrees_prices[4]
        self.add_to_order(item, price)

    def item6(self):
        item = lists.entrees[5]
        price = lists.entrees_prices[5]
        self.add_to_order(item, price)

    def item7(self):
        item = lists.entrees[6]
        price = lists.entrees_prices[6]
        self.add_to_order(item, price)

    def item8(self):
        item = lists.entrees[7]
        price = lists.entrees_prices[7]
        self.add_to_order(item, price)

    def item9(self):
        item = lists.entrees[8]
        price = lists.entrees_prices[8]
        self.add_to_order(item, price)

    def item10(self):
        item = lists.entrees[9]
        price = lists.entrees_prices[9]
        self.add_to_order(item, price)

    def item11(self):
        item = lists.entrees[10]
        price = lists.entrees_prices[10]
        self.add_to_order(item, price)

    def item12(self):
        item = lists.entrees[11]
        price = lists.entrees_prices[11]
        self.add_to_order(item, price)

    def item13(self):
        item = lists.entrees[12]
        price = lists.entrees_prices[12]
        self.add_to_order(item, price)

    def item14(self):
        item = lists.entrees[13]
        price = lists.entrees_prices[13]
        self.add_to_order(item, price)

    def item15(self):
        item = lists.entrees[14]
        price = lists.entrees_prices[14]
        self.add_to_order(item, price)

    def item16(self):
        item = lists.entrees[15]
        price = lists.entrees_prices[15]
        self.add_to_order(item, price)

    def item17(self):
        item = lists.entrees[16]
        price = lists.entrees_prices[16]
        self.add_to_order(item, price)

    def item18(self):
        item = lists.entrees[17]
        price = lists.entrees_prices[17]
        self.add_to_order(item, price)

    def item19(self):
        item = lists.entrees[18]
        price = lists.entrees_prices[18]
        self.add_to_order(item, price)

    def item20(self):
        item = lists.entrees[19]
        price = lists.entrees_prices[19]
        self.add_to_order(item, price)

    def item21(self):
        item = lists.entrees[20]
        price = lists.entrees_prices[20]
        self.add_to_order(item, price)

    def item22(self):
        item = lists.entrees[21]
        price = lists.entrees_prices[21]
        self.add_to_order(item, price)

    def item23(self):
        item = lists.entrees[22]
        price = lists.entrees_prices[22]
        self.add_to_order(item, price)

    def item24(self):
        item = lists.entrees[23]
        price = lists.entrees_prices[23]
        self.add_to_order(item, price)

    def item25(self):
        item = lists.entrees[24]
        price = lists.entrees_prices[24]
        self.add_to_order(item, price)

    def item26(self):
        item = lists.entrees[25]
        price = lists.entrees_prices[25]
        self.add_to_order(item, price)

    def item27(self):
        item = lists.entrees[26]
        price = lists.entrees_prices[26]
        self.add_to_order(item, price)

    def item28(self):
        item = lists.entrees[27]
        price = lists.entrees_prices[27]
        self.add_to_order(item, price)

    def item29(self):
        item = lists.entrees[28]
        price = lists.entrees_prices[28]
        self.add_to_order(item, price)

    def item30(self):
        item = lists.entrees[29]
        price = lists.entrees_prices[29]
        self.add_to_order(item, price)

    def item31(self):
        item = lists.entrees[30]
        price = lists.entrees_prices[30]
        self.add_to_order(item, price)

    def item32(self):
        item = lists.entrees[31]
        price = lists.entrees_prices[31]
        self.add_to_order(item, price)

    def item33(self):
        item = lists.entrees[32]
        price = lists.entrees_prices[32]
        self.add_to_order(item, price)

    def item34(self):
        item = lists.entrees[33]
        price = lists.entrees_prices[33]
        self.add_to_order(item, price)

    def item35(self):
        item = lists.entrees[34]
        price = lists.entrees_prices[34]
        self.add_to_order(item, price)

    def item36(self):
        item = lists.entrees[35]
        price = lists.entrees_prices[35]
        self.add_to_order(item, price)

    def item37(self):
        item = lists.entrees[36]
        price = lists.entrees_prices[36]
        self.add_to_order(item, price)

    def item38(self):
        item = lists.entrees[37]
        price = lists.entrees_prices[37]
        self.add_to_order(item, price)

    def item39(self):
        item = lists.entrees[38]
        price = lists.entrees_prices[38]
        self.add_to_order(item, price)

    def item40(self):
        item = lists.entrees[39]
        price = lists.entrees_prices[39]
        self.add_to_order(item, price)

    def bar_item1(self):
        item = lists.drinks[0]
        price = lists.drinks_prices[0]
        self.add_to_order(item, price)

    def bar_item2(self):
        item = lists.drinks[1]
        price = lists.drinks_prices[1]
        self.add_to_order(item, price)

    def bar_item3(self):
        item = lists.drinks[2]
        price = lists.drinks_prices[2]
        self.add_to_order(item, price)

    def bar_item4(self):
        item = lists.drinks[3]
        price = lists.drinks_prices[3]
        self.add_to_order(item, price)

    def bar_item5(self):
        item = lists.drinks[4]
        price = lists.drinks_prices[4]
        self.add_to_order(item, price)

    def bar_item6(self):
        item = lists.drinks[5]
        price = lists.drinks_prices[5]
        self.add_to_order(item, price)

    def bar_item7(self):
        item = lists.drinks[6]
        price = lists.drinks_prices[6]
        self.add_to_order(item, price)

    def bar_item8(self):
        item = lists.drinks[7]
        price = lists.drinks_prices[7]
        self.add_to_order(item, price)


if __name__ == "__main__":
    myApp = ServerApplication()
    myApp.root.mainloop()

