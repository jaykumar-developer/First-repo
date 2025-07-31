import random

computer = random.randint(1,100)
user = int(input("Guess number : "))

attempt = 1 
while user!=computer:

    if computer>user:
        print("Guesss Higher ")
    else:
        print("Guess Lower")
    user = int(input("Guess another : "))
    attempt+=1
print(f"You guess Right!!!. You guess in {attempt} attempt")

        


        

        
        
        

      

  

  
  


