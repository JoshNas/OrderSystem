import tkinter as tk
import database_functions as dbf


class BarApplication(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('880x980')
        self.root.title("Bar")
        self.window_padding = 8
        self.root['padx'] = self.window_padding

        """Row 1"""
        self.canvas1 = tk.Canvas()
        self.canvas1.grid(row=0, column=0, pady=8)
        tk.Label(self.canvas1, text="Window 1").grid(row=0, column=0)
        tk.Label(self.canvas1, text="Window 2").grid(row=0, column=1)
        tk.Label(self.canvas1, text="Window 3").grid(row=0, column=2)
        tk.Label(self.canvas1, text="Window 4").grid(row=0, column=3)

        self.window1 = tk.Text(self.canvas1, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window1.grid(row=1, column=0)
        self.window2 = tk.Text(self.canvas1, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window2.grid(row=1, column=1)
        self.window3 = tk.Text(self.canvas1, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window3.grid(row=1, column=2)
        self.window4 = tk.Text(self.canvas1, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window4.grid(row=1, column=3)

        tk.Button(self.canvas1, text='Done 1', command=self.delete_window1).grid(row=2, column=0)
        tk.Button(self.canvas1, text='Done 2', command=self.delete_window2).grid(row=2, column=1)
        tk.Button(self.canvas1, text='Done 3', command=self.delete_window3).grid(row=2, column=2)
        tk.Button(self.canvas1, text='Done 4', command=self.delete_window4).grid(row=2, column=3)

        """Row 2"""
        self.canvas2 = tk.Canvas()
        self.canvas2.grid(row=1, column=0, pady=8)
        tk.Label(self.canvas2, text="Window 5").grid(row=0, column=0)
        tk.Label(self.canvas2, text="Window 6").grid(row=0, column=1)
        tk.Label(self.canvas2, text="Window 7").grid(row=0, column=2)
        tk.Label(self.canvas2, text="Window 8").grid(row=0, column=3)

        self.window5 = tk.Text(self.canvas2, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window5.grid(row=1, column=0)
        self.window6 = tk.Text(self.canvas2, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window6.grid(row=1, column=1)
        self.window7 = tk.Text(self.canvas2, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window7.grid(row=1, column=2)
        self.window8 = tk.Text(self.canvas2, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window8.grid(row=1, column=3)

        tk.Button(self.canvas2, text='Done 5', command=self.delete_window5).grid(row=2, column=0)
        tk.Button(self.canvas2, text='Done 6', command=self.delete_window6).grid(row=2, column=1)
        tk.Button(self.canvas2, text='Done 7', command=self.delete_window7).grid(row=2, column=2)
        tk.Button(self.canvas2, text='Done 8', command=self.delete_window8).grid(row=2, column=3)

        """Row 3"""
        self.canvas3 = tk.Canvas()
        self.canvas3.grid(row=2, column=0, pady=8)
        tk.Label(self.canvas3, text="Window 9").grid(row=0, column=0)
        tk.Label(self.canvas3, text="Window 10").grid(row=0, column=1)
        tk.Label(self.canvas3, text="Window 11").grid(row=0, column=2)
        tk.Label(self.canvas3, text="Window 12").grid(row=0, column=3)

        self.window9 = tk.Text(self.canvas3, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window9.grid(row=1, column=0)
        self.window10 = tk.Text(self.canvas3, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window10.grid(row=1, column=1)
        self.window11 = tk.Text(self.canvas3, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window11.grid(row=1, column=2)
        self.window12 = tk.Text(self.canvas3, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window12.grid(row=1, column=3)

        tk.Button(self.canvas3, text='Done 9', command=self.delete_window9).grid(row=2, column=0)
        tk.Button(self.canvas3, text='Done 10', command=self.delete_window10).grid(row=2, column=1)
        tk.Button(self.canvas3, text='Done 11', command=self.delete_window11).grid(row=2, column=2)
        tk.Button(self.canvas3, text='Done 12', command=self.delete_window12).grid(row=2, column=3)

        """Row 4"""
        self.canvas4 = tk.Canvas()
        self.canvas4.grid(row=3, column=0, pady=8)
        tk.Label(self.canvas4, text="Window 13").grid(row=0, column=0)
        tk.Label(self.canvas4, text="Window 14").grid(row=0, column=1)
        tk.Label(self.canvas4, text="Window 15").grid(row=0, column=2)
        tk.Label(self.canvas4, text="Window 16").grid(row=0, column=3)

        self.window13 = tk.Text(self.canvas4, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window13.grid(row=1, column=0)
        self.window14 = tk.Text(self.canvas4, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window14.grid(row=1, column=1)
        self.window15 = tk.Text(self.canvas4, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window15.grid(row=1, column=2)
        self.window16 = tk.Text(self.canvas4, wrap=tk.WORD, bg='#DDDDDD', width=20, height=10)
        self.window16.grid(row=1, column=3)

        tk.Button(self.canvas4, text='Done 13', command=self.delete_window13).grid(row=2, column=0)
        tk.Button(self.canvas4, text='Done 14', command=self.delete_window14).grid(row=2, column=1)
        tk.Button(self.canvas4, text='Done 15', command=self.delete_window15).grid(row=2, column=2)
        tk.Button(self.canvas4, text='Done 16', command=self.delete_window16).grid(row=2, column=3)

    """"Populate order boxes"""
    def populate_boxes(self):
        conn = dbf.create_connection('bar_orders.sqlite3')
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM bar_orders")
            rows = cur.fetchall()
            for i in rows[0]:
                self.window1.insert('end', i)
            for i in rows[1]:
                self.window2.insert('end', i)
            for i in rows[2]:
                self.window3.insert('end', i)
            for i in rows[3]:
                self.window4.insert('end', i)
            for i in rows[4]:
                self.window5.insert('end', i)
            for i in rows[5]:
                self.window6.insert('end', i)
            for i in rows[6]:
                self.window7.insert('end', i)
            for i in rows[7]:
                self.window8.insert('end', i)
            for i in rows[8]:
                self.window9.insert('end', i)
            for i in rows[9]:
                self.window10.insert('end', i)
            for i in rows[10]:
                self.window11.insert('end', i)
            for i in rows[11]:
                self.window12.insert('end', i)
            for i in rows[12]:
                self.window13.insert('end', i)
            for i in rows[13]:
                self.window14.insert('end', i)
            for i in rows[14]:
                self.window15.insert('end', i)
            for i in rows[15]:
                self.window16.insert('end', i)
        except IndexError:
            pass

    """Clears boxes and deletes order"""
    def delete_window1(self):
        num = (self.window1.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window2(self):
        num = (self.window2.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window3(self):
        num = (self.window3.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window4(self):
        num = (self.window4.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window5(self):
        num = (self.window5.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window6(self):
        num = (self.window6.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window7(self):
        num = (self.window7.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window8(self):
        num = (self.window8.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window9(self):
        num = (self.window9.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window10(self):
        num = (self.window10.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window11(self):
        num = (self.window11.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window12(self):
        num = (self.window12.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window13(self):
        num = (self.window13.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window14(self):
        num = (self.window14.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window15(self):
        num = (self.window15.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete_window16(self):
        num = (self.window16.get('1.0', '1.2') + '\n')
        self.delete(num)

    def delete(self, num):
        conn = dbf.create_connection('bar_orders.sqlite3')
        cur = conn.cursor()

        try:
            cur.execute("SELECT * FROM bar_orders WHERE number =?", (num,))
            row = cur.fetchone()

            order_num = row[0]
            time = row[1]
            server = row[2]
            table = row[3]
            order = row[4]

            cur.execute('DELETE FROM bar_orders WHERE number =?', (num,))
            conn.commit()
            dbf.finished_orders_db(order_num, time, server, table, order)
            self.update_boxes()
        except TypeError:
            print('no order')

    def clear_boxes(self):
        self.window1.delete('1.0', 'end')
        self.window2.delete('1.0', 'end')
        self.window3.delete('1.0', 'end')
        self.window4.delete('1.0', 'end')
        self.window5.delete('1.0', 'end')
        self.window6.delete('1.0', 'end')
        self.window7.delete('1.0', 'end')
        self.window8.delete('1.0', 'end')
        self.window9.delete('1.0', 'end')
        self.window10.delete('1.0', 'end')
        self.window11.delete('1.0', 'end')
        self.window12.delete('1.0', 'end')
        self.window13.delete('1.0', 'end')
        self.window14.delete('1.0', 'end')
        self.window15.delete('1.0', 'end')
        self.window16.delete('1.0', 'end')

    def update_boxes(self):
        self.clear_boxes()
        self.populate_boxes()
        myApp.root.after(1000, myApp.update_boxes)


if __name__ == "__main__":
    myApp = BarApplication()
    myApp.update_boxes()
    myApp.root.mainloop()




