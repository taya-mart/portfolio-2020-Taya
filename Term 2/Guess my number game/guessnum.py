#Taya Martinez
#Oct 28
#Guess my number

import random
maxTries=3
rmin=1
rmax=10

def checkNum(message,optmin,optmax):
    while True:
        opt=input(message)
        if opt.isdigit():
            opt=int(opt)
            if opt>=optmin and opt<=optmax:
                return opt
            print("Not a good choice")
        
def menu():
    print("""
                     |menu|
            difficulty level: press 1
              play game: press 2
                   quit: press 3
            """)
    opt=checkNum("Choose an option",1,3)
   
    if opt==1:
        pass
        
    elif press==2:
        guessGame(rmin,rmax,maxTries)



def GetNumInRange(rmin,rmax):
    while True:
        num=input("Enter a whole number from "+str(rmin)+" to "+ str(rmax)+"\n")
        if num.isdigit():
            num= int(num)
            if num >= rmin and num <= rmax:
                return num
        print("Not a good value")

def guessGame(rmin,rmax,maxTries):
    guessCount=0
    TheNumber=random.randint(rmin,rmax)
    while True:
        guessedNum=GetNumInRange(rmin,rmax)
        guessCount +=1
        while guessCount != maxTries and guessedNum != TheNumber:
            if guessedNum>TheNumber:
                print("Guess lower")
            else:
                print("Guess higher")
            guessedNum=GetNumInRange(rmin,rmax)
            guessCount +=1
        if guessedNum==TheNumber:
            print("You've Won!")
            break
        else:
            print("You've Lost")
            break

menu()
