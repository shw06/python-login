from cProfile import label
from cgitb import text
from inspect import getargvalues
from sqlite3 import Row
from tabnanny import check
from tkinter import *
from tkinter import font
from tkinter.tix import COLUMN
root = Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")


root.title("Registration form")
# heading
Label(root, text= "Python registration form", font="Arial 15 bold").grid(row=0, column=3)

# Field names
name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency")
payment_mode = Label(root, text="payment mode")

# packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# variables to store data
namevalue = StringVar
phonevalue = StringVar 
gendervalue = StringVar
emergencyvalue = StringVar
payment_modevalue = StringVar
checkvalue = IntVar

# entry field
nameentry = Entry(root, textvariable= namevalue)
phoneentry = Entry(root, textvariable= phonevalue)
genderentry = Entry(root, textvariable= gendervalue)
emergencyentry = Entry(root, textvariable= emergencyvalue)
payment_modeentry = Entry(root, textvariable= payment_modevalue)

# packing entry field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
payment_modeentry.grid(row=5, column=3)

# checkbox
checkbtn = Checkbutton(text='remember me ?', variable=checkvalue)
checkbtn.grid(row=6, column=3)

# submit button
Button(text='Submit',command=getvals).grid(row=7,column=3)

root.mainloop()