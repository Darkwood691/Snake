
scoreboard = open("scoreboard.txt", "w")
number = int(input("Number: "))

for n in range(number):
    n=number-n
    entry = ("name "+str(n)+"\n")
    scoreboard.write(entry)

scoreboard.close()
print("Done")
