from food_Consumption_Management import foodConsumptionManagement
from tkinter import *
from tkinter import messagebox

def openFood():
    top = Toplevel()
    top.title("Food Consumption Management")
    label1 = Label(top, text="Food Consumption Management", font=("Ariel", 16))
    label1.grid(row=0, column=0, columnspan=5, pady=10)

    entryLabel = Label(top, text="Enter the number of meals available: ", font=("Ariel", 9))
    entryLabel.grid(row=1, column=0, columnspan=5)

    e = Entry(top, width=35, borderwidth=5)
    e.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    def enterNums(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        return

    def clear():
        e.delete(0, END)

    def popup():
        meals = e.get()
        days = foodConsumptionManagement(int(meals))
        messagebox.showinfo("Food Consumption Info", "Current number of meal(s): " + str(meals) +
                            "\nMinimum number of days to consume meal(s): " + str(days))

    button1 = Button(top, text="1", padx=44, pady=20, command=lambda: enterNums(1))
    button2 = Button(top, text="2", padx=44, pady=20, command=lambda: enterNums(2))
    button3 = Button(top, text="3", padx=44, pady=20, command=lambda: enterNums(3))
    button4 = Button(top, text="4", padx=44, pady=20, command=lambda: enterNums(4))
    button5 = Button(top, text="5", padx=44, pady=20, command=lambda: enterNums(5))
    button6 = Button(top, text="6", padx=44, pady=20, command=lambda: enterNums(6))
    button7 = Button(top, text="7", padx=44, pady=20, command=lambda: enterNums(7))
    button8 = Button(top, text="8", padx=44, pady=20, command=lambda: enterNums(8))
    button9 = Button(top, text="9", padx=44, pady=20, command=lambda: enterNums(9))
    button0 = Button(top, text="0", padx=96, pady=20, command=lambda: enterNums(0))
    buttonClear = Button(top, text="Clear", padx=33, pady=20, command=clear)

    button1.grid(row=5, column=1)
    button2.grid(row=5, column=2)
    button3.grid(row=5, column=3)
    button4.grid(row=4, column=1)
    button5.grid(row=4, column=2)
    button6.grid(row=4, column=3)
    button7.grid(row=3, column=1)
    button8.grid(row=3, column=2)
    button9.grid(row=3, column=3)
    button0.grid(row=6, column=1, columnspan=2)
    buttonClear.grid(row=6, column=3)

    buttonSubmit = Button(top, text="Submit", padx=131, pady=10, command=popup)
    buttonSubmit.grid(row=7, column=0, columnspan=5)
