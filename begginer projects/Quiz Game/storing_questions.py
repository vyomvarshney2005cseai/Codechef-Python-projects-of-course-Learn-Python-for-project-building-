import time
import random

def get_questions():
    return [
        {"question": "Which keyword is used to define a function in Python?", 
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        
        {"question": "What is the output of print(2 ** 3) in Python?", 
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},
    ]

def play_quiz():
    print("Welcome to Python Quiz!")

    questions = get_questions()
    
    random.shuffle(questions) 

if __name__ == "__main__":
    play_quiz()