import tkinter
import os
from pixela import Pixela
USERNAME = os.environ.get('PIXEL_USER')
TOKEN = os.environ.get('PIXEL_TOKEN')


def open_graph():
    os.system("open \"\" https://pixe.la/v1/users/brendan/graphs/graph1.html")


def add_pixel():
    pixela = Pixela(USERNAME, TOKEN)
    page_num = page_entry.get()
    print(type(page_num))
    pixela.add_pixel(page_num)


def grid_layout():
    page_label.grid(row=1, column=1)
    page_entry.grid(row=1, column=2)
    website_button.grid(row=2, column=1)
    update_button.grid(row=2, column=2)


window = tkinter.Tk()
window.title('Habbit Tracker - v1.0')
window.config(padx=10, pady=20)
page_entry = tkinter.Entry(width=5, highlightthickness=0)
page_entry.focus()
page_label = tkinter.Label(
    padx=5,
    text='Pages read today:'
    )
website_button = tkinter.Button(
    text='Go to graph',
    command=open_graph
    )
update_button = tkinter.Button(
    text='Add pages',
    command=add_pixel
    )
grid_layout()
window.mainloop()
