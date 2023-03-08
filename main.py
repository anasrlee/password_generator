from tkinter import *
from tkinter import messagebox
import math
from random import randint, choice,shuffle
import pyperclip
FONT_NAME = "Courier"

def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwords_list=[choice(letters) for _ in range (randint(8,10))]
    passwords_list+=[choice(numbers) for _ in range (randint(2,4))]
    passwords_list+=[choice(symbols) for _ in range (randint(2,4))]

    shuffle(passwords_list)

    password="".join(passwords_list)

    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

def save():
    password=password_entry.get()
    website_name=website_entry.get()
    email=email_entry.get()

    if len(password)==0 or len( website_name)==0 :
           messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any field empty.")
    else:
        is_ok=messagebox.askokcancel(title=website_name,message=f"these are the details entered: /n Email: {email}"
        f"\n Password {password}\n its ok to save ?")

    if is_ok:
        with open("passwords.txt", "a") as file_data:
            file_data.write(f"{website_name} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label = Label(text="website:", font=(FONT_NAME, 10))
web_label.grid(column=0, row=1)

email_label = Label(text="Email/User name:", font=(FONT_NAME, 10))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(column=0, row=3)

generate= Button(text="generate password",width=14,command=generate_password)
generate.grid(column=2, row=3)

add_button = Button(text="Add Password", width=37,command=save)
add_button.grid(row=4, column=1, columnspan=2)

website_entry = Entry(width=44)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"anaschaabenemaker93@gmail.com")

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)


window.mainloop()
