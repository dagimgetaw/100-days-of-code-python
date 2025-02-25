from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def save():
    website = website_value.get()
    email = email_value.get()
    password = pass_value.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure u have left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email}\npassword: {password}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_value.delete(0, END)
                pass_value.delete(0, END)


def generate():
    pass_value.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers
    random.shuffle(password_list)
    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)

    pass_value.insert(0, generated_password)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.image = logo

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_value = Entry(width=35)
website_value.grid(row=1, column=1, columnspan=2, pady=5)
website_value.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_value = Entry(width=35)
email_value.grid(row=2, column=1, columnspan=2, pady=5)
email_value.insert(0, "example@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)
pass_value = Entry(width=21)
pass_value.grid(row=3, column=1, pady=5)

generate_pass = Button(text="Generate Password", command=generate)
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
