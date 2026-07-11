import time
import random

def get_python_questions():
    return [
        {"question": "Which keyword is used to define a function in Python?",
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        
        {"question": "What is the output of print(2 ** 3) in Python?", 
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},
        
        {"question": "Which of the following is used to take input from the user?", 
         "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], "answer": "A"},
    ]

def countdown_timer():
    print("\nYou have 10 seconds to think...")
    for i in range(10, 0, -1):
        print(f"\rTime left: {i} seconds  ", end="")
        time.sleep(1)
    print("\nTime's up!\n")


def display_question(question_data, question_number):
    # -------------------- WRITE YOUR CODE HERE ----------------------
    print("\n====================")
    print(f"Question {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)





def play_quiz():
    print("Welcome to Python Quiz!")
    questions = get_python_questions()
    random.shuffle(questions)
    question_number=1
    for question in questions:
        display_question(question,question_number)
        question_number=question_number+1

    # -------------------- WRITE YOUR CODE HERE ----------------------




    

if __name__ == "__main__":
    play_quiz()