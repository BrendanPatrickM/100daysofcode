import tkinter
from tkinter import messagebox
import random
#import pyperclip
STARTING_VALUE = 'brendandotm@gmail.com'


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = random_letter + random_num + random_sym
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_ent.insert(0, password)
    #pyperclip.copy(password)


def layout():
    canvas.grid(column=1, row=0)
    web_label.grid(column=0, row=1)
    web_ent.grid(column=1, row=1, columnspan=2)
    use_label.grid(column=0, row=2)
    use_ent.grid(column=1, row=2, columnspan=2)
    pass_label.grid(column=0, row=3)
    pass_ent.grid(column=1, row=3)
    gen_but.grid(column=2, row=3)
    add_but.grid(column=1, row=4, columnspan=2)


def save():
    website = web_ent.get()
    email = use_ent.get()
    password = pass_ent.get()
    info_string = f'{website} | {email} | {password}\n'

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(message=f'You entered the following\n\n{email}\n{password}\n\nReady to save?')
        if is_ok:
            with open('data.txt', mode='a') as data_file:
                data_file.write(info_string)
            clear_fields()


def clear_fields():
    web_ent.delete(0, len(web_ent.get()))
    pass_ent.delete(0, len(pass_ent.get()))


window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# CANVAS
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
# LABELS
web_label = tkinter.Label(text='Website:')
use_label = tkinter.Label(text='Email/Username:')
pass_label = tkinter.Label(text='Password:')
# ENTRIES
web_ent = tkinter.Entry(width=34)
web_ent.focus()
use_ent = tkinter.Entry(width=34)
use_ent.insert(0, STARTING_VALUE)
pass_ent = tkinter.Entry(width=19)
# BUTTONS
gen_but = tkinter.Button(text='Generate Password', width=11, command=generate_password)
add_but = tkinter.Button(text='Add', width=32, command=save)

layout()
window.mainloop()
