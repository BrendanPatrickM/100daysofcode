from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='this it placeholder question text',
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)