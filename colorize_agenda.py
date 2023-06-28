# Rahul is playing a game, wherein he has multiple coloured wooden blocks, stacked one above the other, his task is to remove all the wooden blocks from the stack, without letting it fall and in the minimum number of steps. He can remove one block of a colour at a time, but he can remove multiple blocks of the same colour together. Determine the minimum number of steps in which he can perform this task.

# For example, if you remove [red,red] from (white,red,red,white), the resulting array is [white,white].

# Note- there are only two colour blocks – red and white

# Function description :

# Complete the minMoves function in the provided editor. It contains the following parameters:

# Parameters:

# Name	Type	Description
# N	Integer	No. of Wooden blocks
# Array[ ]	Integer Array	Array of Blocks.
# Input format :

# The first line contains an integer n denoting the number of blocks. Each n line denotes the colour of the wooden block .

# Constraints :
# 1<=n<=700
# 0<=a[i]<=1

# Sample input 1 :

# 4
# red
# white
# white
# red

# Sample Output 2 :

# 2

# Explanation :

# Remove [white,white] first The array will be [red,red] The remaining numbers can  be removed in one strap .

# Sample Input 1:

# 4
# white
# red
# white
# red

# Sample Output 1:

# 3

# Sample Explanation:
# 0
# The steps are [white,red,white,red]->[red,white,red]->[red,red]->[]. Therefore the answer is 3.


n = int(input())
arr = []

for i in range (n):
    arr.append(input())

current = arr[0]
conut = 0
for i in range(1,n):
    if arr[i] != current:
        conut = conut+1
        current = arr[i]

print(conut)