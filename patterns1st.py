for i in range(1,6):
    print('*' * i)
    
rows = 5    
for i in range(1,6):
    print(" "*(rows-i) + "*" * i)
    

           #OR
           
           
rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
        
        


# A
# AB
# ABC
# ABCD
# ABCDE


rows = 5
for i in range(1,rows+1):
    n=65
    for j in range(1,i+1):
        print(chr(n),end="")
        n+=1
    print()
    
    
# A
# BC
# DEF
# GHIJ
# KLMNO

rows = 5
n = 65

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(n),end="")
        n+=1
    print()


# A
# BB
# CCC
# DDDD
# EEEEE

rows = 5
n = 65

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(n),end="")
    n+=1
    print()


# 1
# AA
# 123
# BBBB
# 12345

rows = 5
n = 65
for i in range(1,rows+1):
    for j in range(1,i+1):
        if i % 2 ==0:
            print(chr(n),end="")
        else:
            print(j,end="")
    if i%2 == 0:
        n+=1
    print()




