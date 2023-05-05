class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_que = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q {self.question_number}: {curr_que.text} (True/False): ")
        self.check_answer(user_ans, curr_que.answer)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print(f"Your answer is correct !")
            self.score += 1
        else:
            print("You got it wrong !!")
        print(f"Correct answer is {corr_ans}")
        print(f"Your Score is {self.score}/{self.question_number}")
        print("\n")