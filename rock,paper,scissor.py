import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
decision=[rock,paper,scissor]
#your decision
decision1=int(input("what do you choose ?enter 0 for rock , 1 for paper , 2 for scissor."))
your_decision=decision[decision1]
#computers decision
computer_selection=random.randint(0,2)
computers_decision=decision[computer_selection]

#game rules
print(f"you chose \n {your_decision}\n")
print(f"computer chose \n{computers_decision}\n")
if decision1==computer_selection:
    print("its a tie")
if decision1==0 and computer_selection==1:
    print("you lose")
if decision1==0 and computer_selection==2:
    print("you win")
if decision1==1 and computer_selection==0:
    print("you win")
if decision1==1 and computer_selection==2:
    print("you lose")
if decision1==2 and computer_selection==0:
    print("you lose")
if decision1==2 and computer_selection==1:
    print('you win')

