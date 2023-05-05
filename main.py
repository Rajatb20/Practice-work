from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    que = i["text"]
    ans = i["answer"]
    question = Question(que,ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.has_questions():
    quiz.next_question()

print("You have completed the quiz !!")
print(f"Your score is {quiz.score}/{quiz.question_number}")