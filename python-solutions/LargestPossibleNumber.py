# Given a list of non-negative numbers arrange them in  such a manner that they form the largest
# number possible.The result is going to be very large Hence return the result in th form of String.

# Input 
# 5            //Value of N=5
# 3 30 34 5 9  // Value of Arr[]={3,30,34,5,9}

# Output
# 9534330

n=int(input())
arr=list(map(int,input().split()))

max_len=len(str(max(arr)))
arr_list = list(map(lambda x: str(x), arr))
final_list = list(map(lambda x: x.ljust(max_len-len(x) + len(x), '0'), arr_list))
arr_list = list(map(lambda x: int(x), final_list))

ans=''
for x in range (n):
	m=max(arr_list)
	index = arr_list.index(m)
	arr_list[index]=0
	ans+=str(arr[index])

print(ans)


# Bug: Not able to give correct output when two or more same number in the list