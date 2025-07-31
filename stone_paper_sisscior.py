import random
'''
1 "Stone"
-1 "sissor"
0 "paper"


'''
computer =random.choice(["stone","paper","sissor"])
you = input("Enter your choice : ")
print(f"computer choice : {computer} , Your choice : {you}")

if computer==you :
    print("Its a draw")

else:
    if computer== """stone""" and you=="sissor":
        print("you lose!")
    elif computer== "stone" and you=="paper":
        print("you win!")

    elif computer== "sissor" and you=="paper":
        print("you lose!")

    elif computer== "sissor" and you=="stone":
        print("you win!")

    elif computer== "paper" and you=="stone":
        print("you lose!")
    elif computer== "paper" and you=="sissor":
        print("you win!")