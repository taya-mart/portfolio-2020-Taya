#taya martinez
#12/19
#midterm

import sys


def open_file(file_name,mode):
    try:
        file=open(file_name,mode)
        return file
    except IOError as e:
        print("unable to open the file",file_name,". Ending program. \n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()


def next_line(the_file):
    line=the_file.readline()
    line=line.strip("\n")
    line=line.replace("/","\n")
    return line


def question_block(the_file):
    category=next_line(the_file)
    question=next_line(the_file)
    answers=[]
    for i in range(4):
        answers.append(next_line(the_file))
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    return category,question,answers,correct,explanation


def welcome(title):
    """Welcome the player to get his or her name"""
    print("\tWelcome to my Python Trivia Challenge!\n")
    print("\tThis test was created by", title,"\n")
    

def get_file_name():
    while True:
        file_name=input("enter in the name of your file including the .txt here: ")
        if ".txt" in file_name and " " not in file_name:
            return file_name
        else:
            print("not a good file name")


def main():
    file_name=get_file_name()
    file=open_file(file_name,"r")
    title=next_line(file)
    name=input("Enter your full name: ")
    questions=0
    score=0
    category,question,answers,correct,explanation=question_block(file)
    welcome(title)
    while category:
        print(category)
        print(question)
        for i in range(len(answers)):
            print("\t",i+1,"-",answers[i])
        answer=input("enter your answer: ")
        #
        if answer==correct:
            print("You betcha!")
            score += 1
            questions += 1
        else:
            print("wrong")
            questions += 1
        print()
        print(explanation)
        print()
        category,question,answers,correct,explanation=question_block(file)
    file.close()
    print("your score is in!")
    input("press enter to see your report card")
    report_card(name,questions,score)


def write_score(name,score):
    file=open_file("scores.txt","a+")
    pair=name+":     "+score+"\n"
    line=[]
    line.append(pair)
    file.writelines(line)
    file.close()


def report_card(name,questions,score):

    points=100/questions
    right=points*score

    print(""""
                            _                       _ 
                           | |                     | |
  _ __ ___ _ __   ___  _ __| |_    ___ __ _ _ __ __| |
 | '__/ _ \ '_ \ / _ \| '__| __|  / __/ _` | '__/ _` |
 | | |  __/ |_) | (_) | |  | |_  | (_| (_| | | | (_| |
 |_|  \___| .__/ \___/|_|   \__|  \___\__,_|_|  \__,_|
          | |                                         
          |_|                                         
""")
    print("student:",name)
    print("you answered",score,"/",questions,"correctly!")
    print("each question was worth",points,"points")
    print("you scored",right,"/","100 points")
    print("you got a",right,"%")

    if right==100:
        print("""
          .d8b.         
        d8'   `8b        db   
        88ooo88       88   
        88~~~88  C8888D 
        88       88       88   
        YP       YP       VP  
        """)
    elif right >=90 and right<100:
        print("""
        .d8b.  
        d8' `8b 
        88ooo88 
        88~~~88 
        88       88 
        YP      YP
        """)
    elif right >=80 and right<90:
        print("""
        d8888b. 
        88  `8D 
        88oooY' 
        88~~~b. 
        88   8D 
        Y8888P'
        """)
    elif right >=70 and right<80:
        print("""
        .o88b. 
        d8P  Y8 
        8P      
        8b      
        Y8b  d8 
         `Y88P' 
        """)
    elif right >=60 and right<70:
        print("""
         .o88b.        
        d8P  Y8        
        8P             
        8b      C8888D 
        Y8b  d8        
         `Y88P'        
        """)
    elif right <60:
        print("""
        d88888b 
        88'     
        88ooo   
        88~~~   
        88      
        YP
        """)
    write_score(name,str(score))


#   ***testing session***
main()
input("press enter to close")



