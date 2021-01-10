from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from os import system


question_bank = []
for item in question_data:
    question_text = item['text']
    question_answer = item['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_master = QuizBrain(question_bank)


while quiz_master.still_has_questions():
    system('clear')
    quiz_master.next_question()

system('clear')
print('Quiz completed!')
print(f'Your final score was: {quiz_master.score}/{len(question_bank)}')
