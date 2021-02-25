import tkinter.messagebox
from tkinter import *

window = Tk()
window.title("Shipley Painters")
window.geometry('700x420')

# The different grids
Label(window, text="Name").grid(row=0)
name = Entry(window)
name.grid(row=0, column=1)
Label(window, text="Email").grid(row=1)
email = Entry(window)
email.grid(row=1, column=1)
Label(window, text="ISBN").grid(row=2)
isbn = Entry(window)
isbn.grid(row=2, column=1)

Label(window, text="Height").grid(row=3)
height = Entry(window)
height.grid(row=3, column=1)

Label(window, text="Length 1").grid(row=4)
length1 = Entry(window)
length1.grid(row=4, column=1)

Label(window, text="Length 2").grid(row=5)
length2 = Entry(window)
length2.grid(row=5, column=1)

Label(window, text="Length 3").grid(row=6)
length3 = Entry(window)
length3.grid(row=6, column=1)

Label(window, text="Length 4").grid(row=7)
length4 = Entry(window)
length4.grid(row=7, column=1)

# The options
paint_choice = IntVar()
paint_choice.set(2)
Radiobutton(window, text="Luxury", variable=paint_choice, value=1).grid(row=8, column=0)
Radiobutton(window, text="Standard", variable=paint_choice, value=2).grid(row=8, column=1)
Radiobutton(window, text="Economy", variable=paint_choice, value=3).grid(row=8, column=2)

# Undercoat option
use_undercoat = IntVar()
undercoat = Checkbutton(window, text="Undercoat", variable=use_undercoat)
undercoat.grid(row=8, column=8)


# Calculation
def perform_calc():
    print(use_undercoat.get())
    paint_quality = paint_choice.get()
    area1 = int(height.get()) * int(length1.get())
    area2 = int(height.get()) * int(length2.get())
    area3 = int(height.get()) * int(length3.get())
    area4 = int(height.get()) * int(length4.get())
    area = int(area1) + int(area2) + int(area3) + int(area4)
    if paint_quality == 1:
        paint_cost = 1.90
    elif paint_quality == 2:
        paint_cost = 1.00
    else:
        paint_cost = 0.60

    if use_undercoat.get():
        paint_cost += 0.50

    total_paint_cost = paint_cost * area

    itemised_total = f"total area = {area} \n"  # appears in the message box
    itemised_total += f"Paint cost = {total_paint_cost}"  # appears in the message box

    digits = []
    for _ in range(1, 11):
        digits.append(isbn.get) % 10
        isbn = isbn // 10
    digits.reverse()

    total = 0
    for scale in range(0, 10):
        total += scale * digits[scale - 1]

    cd = total % 11
    if cd == digits[9]:
        print("Check digit is ok")
    else:
        print("Check digit is invalid")

    if name is None:
        print("Value has not been set")

    # Length Check
    elif len(name) < 2:
        print("Name is too short")

    # Format check
    elif email.find("@") < 0:
        print("Email address is not valid")

    # Message box
    tkinter.messagebox.showinfo("Alert Message", itemised_total)


# def handle_click(event):
#    print("The button was clicked")
#    greeting = "Hello "
#    print("Name: " + entry.get())
#    print("ISBN: " + entry2.get())
#    entry.insert(0, greeting)

# Label(window, text="Name").grid(row=1)
# entry = Entry(window)
# entry.grid(row=1, column=2)

# label5 = tkinter.Label(text="name")
# entry = tkinter.Entry()
# label6 = tkinter.Label(text="ISBN")
# entry2 = tkinter.Entry()
# button1 = tkinter.Button(text="Click me 1!")  # , command=handle_click()

# label5.pack()
# entry.pack()
# label6.pack()
# entry2.pack()
# button1.pack()

Button(window, text="Calculate", command=perform_calc).grid(row=10, column=1)

window.mainloop()
