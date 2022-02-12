import tkinter
import tkinter.messagebox
from random import choice, shuffle, randint
import pyperclip
import json


def search_data():
    search_website = website_entry.get()

    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Error!", message="No data file found.")
    else:
        if search_website in data:
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            tkinter.messagebox.showinfo(title=search_website, message=f"Email: {email} \nPassword: {password} ")
        else:
            tkinter.messagebox.showwarning(title="Error!", message=f"No data for {search_website} website.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_save():
    data = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} \n"

    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }

    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        tkinter.messagebox.showerror(title="Empty field!", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = tkinter.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "greex@onet.pl")
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = tkinter.Button(text="Search", command=search_data)
search_button.grid(row=1, column=2)
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=36, command=data_save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()