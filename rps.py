import random
options=["rock","paper","scissors"]
comp=random.choice(options)
player= input("Enter your choice :")
print("computers choice :",comp)
if player==comp:
    print("It is a tie")
else:
    if player=="rock":
        if comp =="paper":
              print("computer won,because it chose paper")
        else:
             print("player won,because computer chose",comp)
    elif player=="paper":
        if comp =="rock":
              print("player won,because computer chose",comp)
        else:
             print("computer won ,it chose scissors")
             
    elif player=="scissors":
        if comp =="rock":
              print("computer won ,because it chose rock")
        else:
             print("player won,because computer chose",comp)
             