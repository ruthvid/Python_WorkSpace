def prime():
    if number<=1:
        print("Not Prime")
    else:
        factors = 0
        for i in range(1,number+1):
            if number % i == 0:
                factors += 1
        if factors == 2:
            print("Prime Number ..!")
        else:
            print("Not prime number")
        
number = int(input("Enter a number:-- "))
prime()





""" Python Code if The input string is a palindrome..! """


def palindrome(letter):
    if letter[:] == letter[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
    
letter = input("Enter letter: ")
palindrome(letter)





"""  Counting vowels in a string..! """

def count_vowels(s):
    vowels = "aeiou"
    count = sum(1 for ch in s.lower() if ch in vowels)
    print("Number of vowels:", count)

text = input("Enter text: ")
count_vowels(text)












