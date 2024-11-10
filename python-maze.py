import random
from question import route
from question import adventure_questions



def play_adventure(route, adventure_questions):

    while adventure_questions:

        random.shuffle(route)
        current_route_questions = route[0]
        print(current_route_questions)
        answer = input().lower()
        if answer in ['left', 'l', 'L' 'right', 'r', 'R']:
        
            random_question_index = random.randint(0, len(adventure_questions) - 1)
            question = adventure_questions.pop(random_question_index)
            print(question['question'])
            user_answer = input().lower()
            if user_answer in question['answer']:
                print("Correct!")
            else:
                print("Incorrect.")
        else:
            print('Not a valid option. You need to choose: left(l) or right(r)')

       


play_adventure(route, adventure_questions)