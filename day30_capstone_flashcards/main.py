import tkinter
import pandas
import random
LANGUAGE1 = 'French'
LANGUAGE2 = 'English'
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    words_df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    words_df = pandas.read_csv('data/french_words.csv')
to_learn = words_df.to_dict(orient="records")


def layout():
    canvas.grid(row=0, column=0, columnspan=2)
    wrong_but.grid(row=1, column=0)
    right_but.grid(row=1, column=1)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_title, text=LANGUAGE1, fill='black')
    canvas.itemconfig(card_word, text=current_card[LANGUAGE1], fill='black')
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text=LANGUAGE2, fill='white')
    canvas.itemconfig(card_word, text=current_card[LANGUAGE2], fill='white')


def know_word():
    global current_card
    to_learn.remove(current_card)
    words_to_learn_df = pandas.DataFrame(to_learn)
    words_to_learn_df.to_csv('data/words_to_learn.csv')
    next_card()


# Initialise UI
window = tkinter.Tk()
window.title('Flippy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
front_image = tkinter.PhotoImage(file='images/card_front.png')
back_image = tkinter.PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
card_word = canvas.create_text(400, 263, text='',
                               font=('Ariel', 60, 'bold'))
card_title = canvas.create_text(400, 150, text='',
                                font=('Ariel', 40, 'italic'))
right_image = tkinter.PhotoImage(file='images/right.png')
right_but = tkinter.Button(image=right_image, command=know_word,
                           highlightthickness=0, borderwidth=0)
wrong_image = tkinter.PhotoImage(file='images/wrong.png')
wrong_but = tkinter.Button(image=wrong_image, highlightthickness=0,
                           borderwidth=0)

layout()
timer = window.after(3000, flip_card)
next_card()

window.mainloop()
