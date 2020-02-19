import mysql.connector
import tkinter as root
from tkinter import*

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="shoppingcart"
    )
cursor = mydb.cursor()

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
    global left_frame
    global right_frame
    relx = 0
    rely = 0
    male_button.place_forget()
    female_button.place_forget()
    left_frame = Frame(window,width=400, height=742, bg='gray')
    left_frame.place(relx=0.15, rely=0.5, anchor=CENTER)
    right_frame = Frame(window, width=950, height=742, bg='pink')
    right_frame.place(relx=0.645, rely=0.5, anchor=CENTER)

    cursor.execute(""" SELECT * FROM male_products """)
    for row in cursor:
        item = Canvas(right_frame, width=100, height=100, bg='black')
        item.update()

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