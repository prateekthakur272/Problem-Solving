# Raman was playing a game,  he starts with x coins. Now in every step,
#he wins and loses and he has to get the money or pay the money as needed.
#He came in contact with a psychic who can see the future and the Psychic predicted the outcomes after each step.
#Now Raman wants to start the game with the minimum wage where he doesn’t run out of money.
#Help Raman to find what money he should start with. The only rule to keep playing is not going in a credit situation.

# Input Format:

# First line with n, number of steps in the game
# Next n lines, n integers denoting outcomes of every game. Positive means winning and negative means losing that money.
# Output Format:

# One single integer denoting the minimum amount to start with
# Constraints:

# Number of steps<=10^9
# -1000<=Money needed in each step<=1000
# Sample Input:

# 4
# 2
# -9
# 15
# 2

# Sample Output:

# 7

# Explanation:

# If he starts with 7 rupees, then after steps : 7 ->9 -> 0-> 15 -> 17.

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

score,ans = 0,0
for i in arr:
    score = score+i
    if(score<=0):
        ans = (-1*score)+ans
print(ans)
