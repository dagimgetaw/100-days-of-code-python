from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.pack()

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.image = logo

window.mainloop()
