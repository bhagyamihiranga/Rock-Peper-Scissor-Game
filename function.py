import lg as log
import random

def game(user_input):
    
    options = [1,2,3]
    choise = random.choice(options)
    
    if user_input == "rock":
        user_input = 1
    elif user_input == "paper":
        user_input = 2
    elif user_input == "sesor":
        user_input = 3
    
    if user_input == "":
        print("enter somthing to this")
    elif user_input in options:
        
        if user_input == 1:
             if choise == 2:
                 print('you loase computer chose paper')
                 log.log_data('error','Lose')
                 log.log_data('error','Won')
             elif choise == user_input:
                 print('that game was tie')
                 log.log_data('error','Tie')
             else:
                 print('you won compueter chose paper')   
                 log.log_data('error','Won')
        elif user_input == 2:
            if choise == 3:
                print('you lose computer chose sesor')
                log.log_data('error','Lose')
            elif choise == user_input:
                print('that game was tie')
                log.log_data('error','Tie')
            else:
                print('you won compuetr chose sesor')
                log.log_data('error','Won')
        else:
            if choise == 1:
                print('you loss compuet chose rock')
                log.log_data('error','Lose')
            elif choise == user_input:
                print('that was tie')
                log.log_data('error','Tie')
            else:
                print('you won compuet chose rock')
                log.log_data('error','Won')
    else:
        print('you enter wrong option options are (rock,paper,sesior)')
        log.log_data('error','wrong input')
        
    
    
    





