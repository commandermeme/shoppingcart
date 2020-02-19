import time
import sqlite3
import tkinter as root
from tkinter import*

con = sqlite3.connect('mydatabase.db')
cursorObj = con.cursor()
#cursorObj.execute("CREATE TABLE female_products(id integer PRIMARY KEY, product_name text, brand text, price float, stock integer, date_added DateTime)")
# cursorObj.execute("INSERT INTO products VALUES(2, 'Eyeglasses2', 'Rayban', '500', 100, '2019-02-19')")
# con.commit()
# con.close()

window = root.Tk()
window.configure(bg='black')
window.title('Interactive Virtual Shopping')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("{}x{}".format(screen_width, screen_height))

welcome_label = Label(window, font='Calibri 40', bg='black', fg='gray', text='Welcome to Abcd Efgh!')
welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

def shop_now():
    global male_button
    global female_button
    welcome_label.place_forget()
    shopnow_button.place_forget()
    male_button = Button(window, text="Male", command=male_products)
    male_button.place(relx=0.3, rely=0.5, anchor=CENTER)
    female_button = Button(window, text="Female", command=female_products)
    female_button.place(relx=0.6, rely=0.5, anchor=CENTER)

def male_products():
    limit = 1
    x = 0.15
    y = 0.5
    global left_frame
    global right_frame
    male_button.place_forget()
    female_button.place_forget()
    left_frame = Frame(window,width=400, height=742, bg='gray')
    left_frame.place(relx=0.15, rely=0.5, anchor=CENTER)
    right_frame = Frame(window, width=950, height=742, bg='pink')
    right_frame.place(relx=0.645, rely=0.5, anchor=CENTER)

    cursorObj.execute('SELECT * FROM male_products')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
        item = Canvas(right_frame, width=100, height=100)
        item.pack(side=LEFT, padx=5)
        right_frame.pack_propagate(False)
        right_frame.update()

def female_products():
    male_button.place_forget()
    female_button.place_forget()
    left_frame = Frame(window)
    left_frame.place()
    right_frame = Frame(window, bg='gray')
    right_frame.place(relx=0.6, rely=0.5, anchor=E)
    window.configure(bg='pink')

shopnow_button = Button(window, text="Shop now!", command=shop_now)
shopnow_button.place(relx=0.5,rely=0.6, anchor=CENTER)

window.mainloop()