import random
from question import route
from question import adventure_questions as ad



def play_adventure(route, adventure_questions):
    
    chance_list = ["AL"] * 3 + ["FW"] * 6 + ["Q"] * 21
    adventure_questions = ad[:]
    
    distance = 0
    life = 3
    quit_game = ' If you want to exit the game, press "q". But then Python will eat you'

    while adventure_questions and life > 0:

        random.shuffle(route)
        current_route_questions = route[0]
        print(current_route_questions, quit_game)
        answer = input().lower()
        if answer.lower() == "q":
            print()
            life = 0
            print(f"You covered {distance} meters before Python ate you.")
            break
        else:
            
            if answer in ['left', 'l', 'L' 'right', 'r', 'R', 's', 'S', 'straight']:
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_right = chance_list[random_index]
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_left = chance_list[random_index]
                print(way_to_left)
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_straight = chance_list[random_index]

                if answer in ['left', 'l', 'L'] and  way_to_left == "AL":
                    print()
                    print("You chose the right path and found an extra life.")
                    print()
                    life = life + 1
                    print(f"Now you have {life} lifes")
                    print()      
                elif answer in ['left', 'l', 'L'] and  way_to_left == "FW":
                    print()
                    print("This time you were lucky, you found a path without Python")
                    print()
                    print(f"You have advanced {distance} meters deeper into the Python Maze")
                    print()
                else:
                    print()
                    print("You are being attacked by a python!")
                    random_question_index = random.randint(0, len(adventure_questions) - 1)
                    question = adventure_questions.pop(random_question_index)
                    print()
                    print(question['question'], quit_game)

                
                
                user_answer = input().lower()
                if user_answer.lower() == "q":
                    print()
                    life = 0
                    print(f"You covered {distance} meters before Python ate you.")
                    break
                else:
                    if user_answer in question['answer']:

                        print("Correct!")
                        distance = distance + 100

                        print(f"You have advanced {distance} meters deeper into the Python Maze")
                        print()

                    else:
                        print("Incorrect.")

                        life = life - 1

                        if life >= 1:
                            print(f"You've wasted your life. {life} more and the python will eat you.")
                            print()
            else:
                print('Not a valid option. You need to choose: left(l) or right(r)')



    if life > 0:
        print("Congratulations!")
        print()
        print("You finally found the portal that led you out of this labyrinth.")
        print()
        print("There is another great news. You ate Python")
    else:
        print()
        print('You lost your last life and Python ate you.')
            
           
    if not answer == "q" or not user_answer == "q":
        play_again = input("Will you try again? Type 'y' for yes or type 'n' for no: ").lower()
        if play_again == 'y':
            adventure_questions = ad[:]
            play_adventure(route, adventure_questions)
                


play_adventure(route, ad)