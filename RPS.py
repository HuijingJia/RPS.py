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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

result = random.randint(0, 2)  # generate int for computer in order to compare
if result == 0:
    print("Computer chose: ", rock)
elif result == 1:
    print("Computer chose: ", paper)
else:
    print("Computer chose: ", scissors)

row_1 = ["draw", "lose", "win"]
row_2 = ["win", "draw", "lose"]
row_3 = ["lose", "win", "draw"]

map = [row_1, row_2, row_3]
if map[choice][result] == "win":
 print("You win!")
elif map[choice][result] == "lose":
  print("You lose!")
else:
  print("It's a draw.")
