import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock,paper,scissor]
user_choice = int(input("What do you want to choose? type 0 for Rock ,1 for paper ,2 for scissor\n"))
print(game_img[user_choice])
computer_choice = random.randint(0,2)
print(game_img[computer_choice])
print(f"computer choose {computer_choice}")
if user_choice>=3 or user_choice<0:
    print("Invalid number")
elif user_choice == 0 and computer_choice==2:
    print("You Win!")
elif computer_choice==0 and user_choice ==2:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You lose !")
elif user_choice==computer_choice:
    print("It's a draw!")
