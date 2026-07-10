import time
import random

def get_python_questions():
    return [
        {"question": "Which keyword is used to define a function in Python?",
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        
        {"question": "What is the output of print(2 ** 3) in Python?", 
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},
        
        {"question": "Which data type is mutable in Python?", 
         "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"},
        
        {"question": "Which of the following is used to take input from the user?", 
         "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], "answer": "A"},
        
        {"question": "What will be the output of len('Python')?",
         "options": ["A) 5", "B) 6", "C) 7", "D) Error"], "answer": "B"}
    ]



def countdown_timer():
    # -------------------- WRITE YOUR CODE HERE ----------------------
    print("\nYou have 10 seconds to think...")
    time.sleep(1)
    for i in range(10, -1, -1):
        print(f"\rTime left: {i} seconds ", end="")
        time.sleep(1)
    print("\nTime's up!\n")

    
def play_quiz():
    print("Welcome to Python Quiz!")
    questions = get_python_questions()
    random.shuffle(questions)

    countdown_timer()

if __name__ == "__main__":
    play_quiz()