# Question 4 :Make It Palindrome
# Problem Statement  :

# You’re given a string, you’ve to print additional characters needed to make that string a palindrome.

# A Palindrome is a sequence of characters that has the property of reading the same in either direction.

# Input :
# abede
# Output :
# ba

# Sample Input :
# abcfe

# Sample output :
# fcba


string = input()
def is_pelendrome(string):
    return string == string[::-1]


def make_pelendrome(string):
    if is_pelendrome(string):
        return ""
    for i in range(len(string)):
        rem = string[:i][::-1]
        if is_pelendrome(string+rem):
            return rem
        
print(make_pelendrome(string))