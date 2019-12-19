puzzle = """LINTEGERSTUPLEZIWOENANTRETMRSBSNBOOLEANIDLEWGTFUNCTIONBOISAICFLOATINGPOINTMSVARIABLESPBHEPTSRCIXGDYAAIAXORSTTOFRWGQRNUCRIZRAEMTZGPAAWETNAEBTXMXUVMRHPPGGTRLETEBREYITYYNUHGOMFNOTFLFTTERBJMCEITELEZHMSNVZMWKNLRSOAOAUHJJEXLATEXINN"""
puzzle = puzzle.replace(" ", "")
columns=15
rows=15

##0-14
##15-29
##30-44
##45-59
##60-74
##
##75-89
##90-104
##105-119
##120-134
##135-149
##
##150-164
##165-179
##180-194
##195-209
##210-224


WORDS = ["PYTHON" , #(149,164,179,194,209,224)
                 "BINARY", #(86,101,116,131,146,161)
                 "IDLE", #(39,40,41,42)
                 "INTEGERS", #(1,2,3,4,5,6,7,8,9)
                 "FLOATING POINT", #(61,62,63,64,65,66,67,68,69,70,71,72,73)
                 "BOOLEAN", #(32,33,34,35,36,37,38)
                 "STRING", #(90,105,120,135,150)
                 "VARIABLES", #(76,77,78,79,80,81,82,83,84)
                 "STATEMENT", #(91,107,123,139,155,171,187,203,219)
                 "COMMENT", #(93,109,125,141,157,173,189)
                 "LIST", #(0,15,30,45)
                 "FUNCTION", #(46,47,48,49,50,51,52,53)
                 "TUPLE", #(9,10,11,12,13)
                 "EXCEPT", #(88,103,118,133,148)
                 "IMPORT", #(59,74,89,104,119,134)
                 "RETURN", #(122,137,152,167,182,197)
                 "BLOCK", #(138,154,170,186,202)
                 "WHILE", #(132,147,162,177,192)
                 "PARAMETER", #(85,100,115,130,145,160)
                 "TEXT FILE" #(108,124,140,156,172,188,204,220)
                ]

QUESTIONS = ["what programming language are we learning in this class?",
                          "what computer language consists of 0s and 1s?",
                          "which IDE comes pre-downloaded with Python?",
                          "what data type are whole numbers?",
                          "what data type are numbers with decimals?",
                          "what data type has only 2 possible values being True or False?",
                          "what data type can store a line of text or individual characters  /and must be wrapped in quotes?",
                          "where do programs store specific data values in?",
                          "what is 1 line of code that can be an expression or several words?",
                          "what statement starts with the hash character # ?",
                          "which data structure is a sequence that can be changed /and wrapped in square brackets [] ?",
                          "What is a block of code that only runs when it is called?",
                          "which data structure is a sequence that cannot be changed /and is wrapped in parantheses () ?",
                          "which command catches the exception in a 'try' statement and returns it?",
                          "which command brings in an external module so its functions can be used in a particular script?",
                          "what outputs the value returned by a function and is usually the last step of a function?",
                          "what is a section of code which is grouped together with the same indents called?",
                          "what statement executes a block of code as long as its condition is True?",
                          "what is an argument that a function can accept called?",
                          "what can we read from and write to within Python even though the file is not in Python?"
                        ]

words = ["PYTHON" , 
                 "BINARY", 
                 "IDLE", 
                 "INTEGERS", 
                 "FLOATING POINT", 
                 "BOOLEAN", 
                 "STRING", 
                 "VARIABLES",
                 "STATEMENT", 
                 "COMMENT", 
                 "LIST", 
                 "FUNCTION", 
                 "TUPLE", 
                 "EXCEPT", 
                 "IMPORT", 
                 "RETURN", 
                 "BLOCK", 
                 "WHILE",
                 "PARAMETER", 
                 "TEXT FILE" 
                ]

questions = ["what programming language are we learning in this class?",
                          "what computer language consists of 0s and 1s?",
                          "which IDE comes pre-downloaded with Python?",
                          "what data type are whole numbers?",
                          "what data type are numbers with decimals?",
                          "what data type has only 2 possible values being True or False?",
                          "what data type can store a line of text or individual characters  /and must be wrapped in quotes?",
                          "where do programs store specific data values in?",
                          "what is 1 line of code that can be an expression or several words?",
                          "what statement starts with the hash character # ?",
                          "which data structure is a sequence that can be changed /and wrapped in square brackets [] ?",
                          "What is a block of code that only runs when it is called?",
                          "which data structure is a sequence that cannot be changed /and is wrapped in parantheses () ?",
                          "which command catches the exception in a 'try' statement and returns it?",
                          "which command brings in an external module so its functions can be used in a particular script?",
                          "what outputs the value returned by a function and is usually the last step of a function?",
                          "what is a section of code which is grouped together with the same indents called?",
                          "what statement executes a block of code as long as its condition is True?",
                          "what is an argument that a function can accept called?",
                          "what can we read from and write to within Python even though the file is not in Python?"
                        ]



##def display1(puzzle):
##    a=0
##    b=29
##    puzzle=puzzle.replace("", "|")
##    for i in range(15):
##        print(puzzle[a:b])
##        a+=30
##        b+=30



#displaying puzzle
def display_puzzle(puzzle,columns,rows):
    i = 0
    print("     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14")
    
    for col in range(columns):
        if col < 10:
            line = str(col)+"  | "
        else:
            line = str(col)+" | "
         
        for row in range(rows):
            line += puzzle[i]+" | "
            i += 1
        print(line)        


#get questions and anwers
picked=[]    
def Q_and_A(puzzle,words,questions,picked):
    import random
    while True:
        pick=random.randint(0,len(words)-1)
        if pick not in picked:
            q=questions[pick]
            a=words[pick]
            picked.append(pick)
            return q, a



#grab words
def build(puzzle):
    nums = []
    number = ""
    pos = input("enter the index postitions here--please seperate with a comma , : ")
    for i in pos:
        if i != ",":
            number = number + i
        else:
            if number.isdigit():
                nums.append(int(number))
                number = ""  
    nums.append(int(number))
    if nums[0]+1==nums[1] or nums[0]+15==nums[1] or nums[0]+16==nums[1]:
        word = ""
        while nums:
            x = nums.pop(0)
            word = word + puzzle[x]
        return word


#run
def main(puzzle,picked,words,questions):
    display_puzzle(puzzle,columns,rows)
    count=0
    while count != len(questions):
        x=Q_and_A(puzzle,words,questions,picked)
        print(x[0])
        w=build(puzzle)
        print(w)
        count +=1
    print("Congratulations, you've finished the word search!")




main(puzzle,picked,words,questions)













##display_puzzle(puzzle,columns,rows)
##x=build(puzzle)
##print(x)
#test Q_and_A
##count=0
##while count !=20:
##    q,a=Q_and_A(puzzle,words,questions,picked)
##    print(q,a)
##input()
