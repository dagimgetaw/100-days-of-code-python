from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.image = logo

# Labels and Entries
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_value = Entry(width=35)
website_value.grid(row=1, column=1, columnspan=2, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_value = Entry(width=35)
email_value.grid(row=2, column=1, columnspan=2, pady=5)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_value = Entry(width=21)
pass_value.grid(row=3, column=1, pady=5)

# Buttons
generate_pass = Button(text="Generate Password")
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
