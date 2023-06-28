# Problem statement: Rocky is a software engineer and he is creating his own operating system called “myFirst os”.
#myFirst os is a GUI (Graphical user interface) based operating system where everything is stored in files and folders.
#He is facing issues on  creating unique folder names for the operating system .
#Help rocky to create the unique folder name for it’s os.
#If folder name already exists in the system and integer number is added at the name to make it unique.
#The integer added starts with 1 and is incremented by 1 for each new request of an existing folder name.
#Given a list of folder names , process all requests and return an array of corresponding folder names.

# Example 

# n=5
# foldername= [‘home’ , ‘myfirst’ ,’downloads’, ‘myfirst’, ‘myfirst’]
# Foldername[0] = ‘home’ is unique.
# Foldername[1] = ‘myfirst’ is unique.
# foldername [2] =’downloads’ is unique.
# Foldername[3] =’myfirst’ already exists in our system. So Add1 at the end of the folder name i.e foldername[3] =”myfirst1″
# Foldername[4 ]=’myfirst’ also already exists in our system.So add 2 at the end of the folder name i.e. foldername[4]=”myfirst2″.
# Function description 

# Complete the function folderNameSystem In the editor below
# folderNameSystem has the following parameters
# string foldername[n]: an array of folder name string in the order requested
# Returns:

# String[n]:  an array of strings usernames in the order assigned
# Constraints

#     1<=n<=10^4
#     1<=length of foldername[i]<20
#     foldername[i] contains only lowercase english letter in the range ascii[a-z]
# Input Format:

# The first line contains an integer n , denoting the size of the array usernames Each line i of the n subsequent lines (where i<=0<=n) contains a string usernames[i] representing a username request in the order received.
# Sample case 0

# 4
# home 
# download
# first
# first
# Sample Output 0

# home
# download
# first
# first1
# Explanation 0

#    foldername[0] = ‘home’ is unique
#    foldername[1]=’download’ is unique
#    foldername[2]= ‘first’ is unique
#    foldername[3]=’first’ is already existing . so add 1 to it and it become first1

n=int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n):
    if arr[:i+1].count(arr[i])>1:
        print(arr[i]+str(arr[:i+1].count(arr[i])-1))
    else:
        print(arr[i])
