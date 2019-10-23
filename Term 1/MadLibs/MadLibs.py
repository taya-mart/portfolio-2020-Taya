#Taya Martinez
#9/9/19
#MadLibs

#input variables
bodypart1=input("name a body part?")
verb1=input("add a verb:")
adj1=input("add an adjective:")
color=input("add a color:")
verb2=input("add another verb:")          
noun2=input("add an noun:")
bodypart2=input("name another body part:")
verb3=input("add another verb:")
adj2=input("add another adjective:")
bodypart3=input("name another bodypart:")
bodypart4=input("name another bodypart:")
animal=input("name an animal:")                


#print statement
print(" ")
print(" ")
print(" ")
print(" ")
print("--A TRIP TO THE DOCTOR--")
print(" ")
print(str.format("The other day, I woke up and my {} was sore.",bodypart1))
print(str.format("I looked in the mirror and started to {}.", verb1))
print(str.format("My skin was all {} and there were little {} spots all aver it!", adj1, color))
print(str.format("My dad told me not to {} and took me to the doctor.", verb2))
print(str.format("When we got there, the nurse stuck a {} into my {} to take my temperature.", noun2, bodypart2))
print(str.format("Then she told me to {} for one minute while she got the doctor.", verb3))
print(str.format("The doctor was a/an {} woman with bad breath and a cold {} that she pressed on my {}.", adj2, bodypart3, bodypart4)) 
print(str.format("She said I had the worst case of the {} pox she had ever seen!", animal))

#to open from desktop
input()
