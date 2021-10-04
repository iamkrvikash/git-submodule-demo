# Given a list of non-negative numbers arrange them in  such a manner that they form the largest
# number possible.The result is going to be very large Hence return the result in th form of String.

# Input 
# 5            //Value of N=5
# 3 30 34 5 9  // Value of Arr[]={3,30,34,5,9}

# Output
# 9534330


from itertools import permutations
#Inputs
n=int(input())
arr=list(map(int,input().split()))
#Your Code
res = int(max((''.join(i) for i in permutations(str(i)  for i in arr)), key = int))  

#Output 
print(res)