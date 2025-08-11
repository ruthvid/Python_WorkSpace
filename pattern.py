# task 1

rows = 5
for i in range(1,rows+1):
    c = 65
    s = 97
    if i % 2 ==0:
        for j in range (1,i+1):
            print(chr(s),end="")
            s+=1
    else:
        for j in range (1,i+1):
            print(chr(c),end="")
            c+=1
    print()
    
# Output:--
# A
# ab
# ABC
# abcd
# ABCDE


    
# task 2

rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
    
# Output:--
#     1
#    12
#   123
#  1234
# 12345




# task 3

rows = 5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for j in range(1,i+1):
        print(i,end="")
    print()

# Output:--
#     1
#    22
#   333
#  4444
# 55555


# task 4

rows= 5
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    n = 65
    for j in range(1,i+1):
        print(chr(n),end="")
        n+=1
    print()

# Output:--
#     A
#    AB
#   ABC
#  ABCD
# ABCDE

# task 5

rows = 5

for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    n = 65
    if i % 2 ==0:
        for j in range(1,i+1):
            print(j,end="")
    else:
        for j in range(1,i+1):
            print(chr(n),end="")
            n+=1
    print()

# Output:--
#     A
#    12
#   ABC
#  1234
# ABCDE
