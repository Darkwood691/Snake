
scoreboard = open("scoreboard.txt", "w")
number = int(input("Number: "))

for n in range(number):
    if n%2==0:
        n=str(n)
        entry = ("name "+n+"\n")
        scoreboard.write(entry)
        
for n in range(number):
    if n%2!=0:
        n=str(n)
        entry = ("name "+n+"\n")
        scoreboard.write(entry)
        
scoreboard.close()
print("Done")
