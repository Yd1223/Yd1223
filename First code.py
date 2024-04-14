import random as rd

print("\t\tGuess The Number")

def randNum():
    initNum = int(input("Enter the initial number: "))
    topNum = int(input("Enter the the final number: "))
    return rd.randint(initNum, topNum)
#------------------

randomNum = randNum()

while True:
    guess = int(input("\n\tGuess: "))
    if randomNum == guess:
        print("\t\t\t\tYou got it!!!")
        ans = input("Do you want to continue (say y/n)? ")
        if ans.lower() != 'y':
            break
        else:
            randomNum = randNum()
    else: 
        print("\tYou lost it!!!")
        
        

        
