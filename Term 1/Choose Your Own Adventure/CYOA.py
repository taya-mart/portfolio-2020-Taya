from asciiart import *
from SecretofthePyramidsAllPages import *

print(intro)
print(pagetitle_art)
input("Press enter to read: ")
print(page1_art)
print(pg1)
input("Press Enter to continue: ")
print(pg2)

def choice(page1, page2):
    page1 = str(page1)
    page2 = str(page2)
    while True:
        choice = input("Enter either page " + page1 + " or page " + page2 + "\n")
        if choice == page1:
            return page1
        elif choice == page2:
            return page2
        else:
            print("Sorry that is not an option.")
            continue


def pg1():
    print(intro)
    print(pagetitle_art)
    input("Would You Like to read?")
    print(page1_art)
    print(pg1)
pg1()
def pg2():
    print(page3_art)
    print(pg2)
pg2()

choicex= choice(13,4)
if choicex== "13":
    print(pg13)
if choicex == "4":
    print(pg4)
