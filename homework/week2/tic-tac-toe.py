# Week2 - Day1 Homework
# 2 + 3n * "-"
f = open('tic-tac-toe.txt', "w+")
n = 2

for i in range(2):
    for j in range(n):
        print (" "*(n+1), "|", " "*(n+1), "|", file=f)
    print("- " * ((n+1)*2+n), file=f)
    
for j in range(n):
    print (" "*(n+1), "|", " "*(n+1), "|", file=f)

f.close()