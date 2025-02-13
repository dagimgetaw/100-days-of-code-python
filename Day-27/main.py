from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(width=300, height=200)


def button_clicked():
    new_text = value.get()
    my_label.config(text=new_text)


my_label = Label(text="I am label", font=("Arial", 15))
my_label.grid(row=0, column=0)

button = Button(text="click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="click me", command=button_clicked)
new_button.grid(row=0, column=2)

value = Entry(width=10)
value.grid(row=2, column=4)

window.mainloop()
