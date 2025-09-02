number=int(input("Enter name :-- "))
result = "Prime number" if number >=2 and len([i for i in range(1,number+1) if number%i == 0]) == 2 else "Not prime"
print(result)