import random

number = int(input("Number: "))
scoreboard = open("scoreboard.txt","w")

for n in range(number):
    x=random.randint(0,number)
    entry = ("Name "+str(x)+"\n")
    scoreboard.write(entry)
    
scoreboard.close()
print("Done")
