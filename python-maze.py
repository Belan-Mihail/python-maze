import random
import time
import colorama
from question import route
from question import adventure_questions as ad

from colorama import Fore, Style
colorama.init(autoreset=True)

def play_adventure(route, adventure_questions):
    
    chance_list = ["AL"] * 5 + ["FW"] * 10 + ["Q"] * 50
    adventure_questions = ad[:]
    
    
    distance = 0
    life = 3
    quit_game = '(if you want to exit the game, press "q". But then Python will eat you)'
    loop_count = 0

    while adventure_questions and life > 0:

        random.shuffle(route)
        current_route_questions = route[0]
        loop_count += 1
        if loop_count < 2:
            print() 
            print() 
            print() 
            print() 
            print() 
            print() 
            print()
            print() 
            print() 
            print() 
            print() 
            print() 
            print() 
            print() 
            print() 
            print() 
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
            print()
            time.sleep(0.5)
        else:
            print()  
        time.sleep(0.5)
        print(f"{Style.BRIGHT}{Fore.YELLOW}{current_route_questions}\n{Style.DIM}{Fore.LIGHTYELLOW_EX}{quit_game}")
        time.sleep(0.5)
        answer = input().lower()
        if answer.lower() == "q":
            print()
            time.sleep(0.5)
            life = 0
            print(f"{Style.BRIGHT}{Fore.YELLOW}You covered {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters before Python ate you.")
            break
        else:
            
            if answer in ['left', 'l', 'L' 'right', 'r', 'R', 's', 'S', 'straight']:
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_right = chance_list[random_index]
                
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_left = chance_list[random_index]
                
                
                random.shuffle(chance_list)
                random_index = random.randint(0, len(chance_list) - 1)
                way_to_straight = chance_list[random_index]
                

                if answer in ['left', 'l', 'L'] and  way_to_left == "AL":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.GREEN}You chose the right path and found an extra life.")
                    time.sleep(0.5)
                    life = life + 1
                    print(f"{Style.BRIGHT}{Fore.YELLOW}Now you have {Style.BRIGHT}{Fore.GREEN}{life}{Style.BRIGHT}{Fore.YELLOW} lifes")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance}{Style.BRIGHT}{Fore.YELLOW} meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}right to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_right == "AL" else (Style.BRIGHT + Fore.YELLOW + 'free path') if way_to_right == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.YELLOW + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    time.sleep(0.5)
                    
                elif answer in ['left', 'l', 'L'] and  way_to_left == "FW":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}This time you were lucky, you found a path without Python")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced{Style.BRIGHT}{Fore.GREEN} {distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}right to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_right == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_right == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    time.sleep(0.5)
                    
                elif answer in ['left', 'l', 'L'] and  way_to_left == "Q":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.RED}You are being attacked by a python!")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}right to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_right == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_right == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    print()
                    time.sleep(0.5)
                    random_question_index = random.randint(0, len(adventure_questions) - 1)
                    question = adventure_questions.pop(random_question_index)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}{question['question']}\n{Style.DIM}{Fore.LIGHTYELLOW_EX}{quit_game}")
                    print()
                    time.sleep(0.5)
                    user_answer = input().lower()
                    if user_answer.lower() == "q":
                        time.sleep(0.5)
                        life = 0
                        print(f"{Style.BRIGHT}{Fore.YELLOW}You covered{Style.BRIGHT}{Fore.GREEN} {distance} {Style.BRIGHT}{Fore.YELLOW}meters before Python ate you.")
                        time.sleep(0.5)
                        break
                    else:
                        if user_answer in question['answer']:
                            print()
                            time.sleep(0.5)
                            print(f"{Style.BRIGHT}{Fore.GREEN}Correct!")
                            time.sleep(0.5)
                            distance = distance + 100
                            print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                            time.sleep(0.5)
                            
                        else:
                            print()
                            time.sleep(0.5)
                            print(f"{Style.BRIGHT}{Fore.RED}Incorrect.")
                            time.sleep(0.5)
                            life = life - 1

                            if life >= 1:
                                print(f"{Style.BRIGHT}{Fore.YELLOW}You've wasted your life. {Style.BRIGHT}{Fore.RED}{life} {Style.BRIGHT}{Fore.YELLOW}more and the python will eat you.")
                                time.sleep(0.5)
                                

                if answer in ['right', 'r', 'R'] and  way_to_right == "AL":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.GREEN}You chose the right path and found an extra life.")
                    time.sleep(0.5)
                    life = life + 1
                    print(f"{Style.BRIGHT}{Fore.YELLOW}Now you have {Style.BRIGHT}{Fore.GREEN}{life} {Style.BRIGHT}{Fore.YELLOW}lifes")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)      
                    print(f"{Style.BRIGHT}{Fore.YELLOW}left to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_left == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_left == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)    
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    time.sleep(0.5)    

                elif answer in ['right', 'r', 'R'] and  way_to_right == "FW":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}This time you were lucky, you found a path without Python")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}left to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_left == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_left == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5) 
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    time.sleep(0.5) 

                elif answer in ['right', 'r', 'R'] and  way_to_right == "Q":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.RED}You are being attacked by a python!")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}left to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_left == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_left == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}straight to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_straight == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_straight == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    print()
                    time.sleep(0.5)   
                    random_question_index = random.randint(0, len(adventure_questions) - 1)
                    question = adventure_questions.pop(random_question_index)
                    print(f"{Style.BRIGHT}{Fore.YELLOW}{question['question']}\n{Style.DIM}{Fore.LIGHTYELLOW_EX}{quit_game}")
                    print()
                    time.sleep(0.5)
                    user_answer = input().lower()
                    if user_answer.lower() == "q":
                        time.sleep(0.5)
                        life = 0
                        print(f"{Style.BRIGHT}{Fore.YELLOW}You covered {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters before Python ate you.")
                        time.sleep(0.5)
                        break
                    else:
                        if user_answer in question['answer']:
                            print()
                            time.sleep(0.5)
                            print(f"{Style.BRIGHT}{Fore.GREEN}Correct!")
                            time.sleep(0.5)
                            distance = distance + 100
                            print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                            time.sleep(0.5)

                        else:
                            print()
                            time.sleep(0.5)
                            print(f"{Style.BRIGHT}{Fore.RED}Incorrect.")
                            time.sleep(0.5)
                            life = life - 1
                            
                            if life >= 1:
                                print(f"{Style.BRIGHT}{Fore.YELLOW}You've wasted your life. {Style.BRIGHT}{Fore.RED}{life} {Style.BRIGHT}{Fore.YELLOW}more and the python will eat you.")
                                time.sleep(0.5)


                if answer in ['straight', 's', 'S'] and  way_to_straight == "AL":
                    print()
                    time.sleep(0.5)
                    print(f"{Style.BRIGHT}{Fore.GREEN}You chose the right path and found an extra life.")
                    time.sleep(0.5)
                    life = life + 1
                    print(f"{Style.BRIGHT}{Fore.YELLOW}Now you have {Style.BRIGHT}{Fore.GREEN}{life} {Style.BRIGHT}{Fore.YELLOW}lifes")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"{Style.BRIGHT}{Fore.YELLOW}You have advanced {Style.BRIGHT}{Fore.GREEN}{distance} {Style.BRIGHT}{Fore.YELLOW}meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print(f"{Style.DIM}{Fore.WHITE}other paths led you:") 
                    time.sleep(0.5)   
                    print(f"{Style.BRIGHT}{Fore.YELLOW}left to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_left == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_left == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")  
                    time.sleep(0.5)  
                    print(f"{Style.BRIGHT}{Fore.YELLOW}right to {(Style.BRIGHT + Fore.GREEN + 'extra life') if way_to_right == "AL" else (Style.BRIGHT + Fore.WHITE + 'free path') if way_to_right == "FW" else (Style.BRIGHT + Fore.RED + 'battle with the python')}")
                    time.sleep(0.5)  

                elif answer in ['straight', 's', 'S'] and  way_to_straight == "FW":
                    print()
                    time.sleep(0.5)
                    print("This time you were lucky, you found a path without Python")
                    time.sleep(0.5)
                    distance = distance + 100
                    print(f"You have advanced {distance} meters deeper into the Python Maze")
                    print()
                    time.sleep(0.5)
                    print("other paths led you:") 
                    time.sleep(0.5)     
                    print(f"left to {"extra life" if way_to_left == "AL" else "free path" if way_to_left == "FW" else "battle with the python"}")  
                    time.sleep(0.5) 
                    print(f"right to {"extra life" if way_to_right == "AL" else "free path" if way_to_right == "FW" else "battle with the python"}")
                    time.sleep(0.5) 

                elif answer in ['straight', 's', 'S'] and  way_to_straight == "Q":
                    print()
                    time.sleep(0.5)
                    print("You are being attacked by a python!")
                    print()
                    time.sleep(0.5)
                    print("other paths led you:") 
                    time.sleep(0.5)    
                    print(f"left to {"extra life" if way_to_left == "AL" else "free path" if way_to_left == "FW" else "battle with the python"}")  
                    time.sleep(0.5) 
                    print(f"right to {"extra life" if way_to_right == "AL" else "free path" if way_to_right == "FW" else "battle with the python"}")
                    print()
                    time.sleep(0.5) 
                    random_question_index = random.randint(0, len(adventure_questions) - 1)
                    question = adventure_questions.pop(random_question_index)
                    print(f"{question['question']}\n{quit_game}")
                    print()
                    time.sleep(0.5)
                    user_answer = input().lower()
                    if user_answer.lower() == "q":
                        time.sleep(0.5)
                        print()
                        life = 0
                        print(f"You covered {distance} meters before Python ate you.")
                        time.sleep(0.5)
                        break
                    else:
                        if user_answer in question['answer']:
                            print()
                            time.sleep(0.5)
                            print("Correct!")
                            time.sleep(0.5)
                            distance = distance + 100
                            print(f"You have advanced {distance} meters deeper into the Python Maze")
                            time.sleep(0.5)

                        else:
                            print()
                            time.sleep(0.5)
                            print("Incorrect.")
                            time.sleep(0.5)
                            life = life - 1

                            if life >= 1:
                                print(f"You've wasted your life. {life} more and the python will eat you.")
                                time.sleep(0.5)
            else:
                time.sleep(0.5)
                print()
                print('Not a valid option. You need to choose: left(l) or right(r)')



    if life > 0:
        time.sleep(0.5)
        print()
        print("Congratulations!")
        time.sleep(0.5)
        print()
        print("You finally found the portal that led you out of this labyrinth.")
        time.sleep(0.5)
        print()
        print("There is another great news. You ate Python")
    else:
        if not answer == "q" and not user_answer == "q":
            time.sleep(0.5)
            print()
            print('You lost your last life and Python ate you.')
            time.sleep(0.5)
            print()
        else:
            time.sleep(0.5)
            print()
            print('you tried to escape the maze but Python ate you')
            
           
    if not answer == "q" and not user_answer == "q":
        play_again = input("Will you try again? Type 'y' for yes or type 'n' for no: ").lower()
        if play_again == 'y':
            adventure_questions = ad[:]
            play_adventure(route, adventure_questions)
                


play_adventure(route, ad)