from tkinter import *

window = Tk()
window.title("Mile to kiloMeter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)


def calculate():
    distance = value.get()
    final_value = round(float(distance) * 1.60934)
    kilometer.config(text=final_value)


my_label = Label(text="is equal to", font=("Arial", 12))
my_label.grid(row=4, column=3)

kilometer = Label(text="0", font=("Arial", 10))
kilometer.grid(row=4, column=4)

km = Label(text="Km", font=("Arial", 10))
km.grid(row=4, column=5)

value = Entry(width=10)
value.grid(row=2, column=4)

ml = Label(text="Miles", font=("Arial", 10))
ml.grid(row=2, column=5)

button = Button(text="Calculate", command=calculate)
button.grid(row=5, column=4)

window.mainloop()
