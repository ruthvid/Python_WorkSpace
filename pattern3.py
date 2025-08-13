rows = 5
for i in range(rows,0,-1):
    print(" "*(rows-i),end="")
    n = 65
    for j in range(i):
        if i ==5:
            print(chr(n),end="")
        elif i == 4 :
            print(chr(n+1),end="")
        else:
            print(chr(n),end="")
            n+=1
    print()