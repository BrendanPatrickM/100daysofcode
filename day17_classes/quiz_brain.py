class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f'Score: {self.score}')
        user_answer = input(f'Q.{self.question_number}: {current_question.text}:\
                        True or False? \n').lower()
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if user_answer == correct_answer.lower():
            print('Correct!')
            self.score += 1
        else:
            print('Incorrect')
