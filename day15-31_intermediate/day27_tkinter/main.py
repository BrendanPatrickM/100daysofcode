import tkinter


def convert():
    m_to_convert = float(entry.get())
    km = m_to_convert * 1.60934
    label3.config(text=km)


def layout():
    entry.grid(column=1, row=0)
    label1.grid(column=2, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=1, row=1)
    label4.grid(column=2, row=1)
    calculate.grid(column=1, row=2)


window = tkinter.Tk()
window.title('Miles to KM Converter')
window.config(padx=20, pady=20)
# Entries
entry = tkinter.Entry(width=5)
entry.focus()
# Labels
label1 = tkinter.Label(text='Miles')
label2 = tkinter.Label(text='is equal to')
label3 = tkinter.Label(text='0')
label4 = tkinter.Label(text='Km')
# Buttons
calculate = tkinter.Button(text='Calculate', command=convert)
layout()

window.mainloop()
