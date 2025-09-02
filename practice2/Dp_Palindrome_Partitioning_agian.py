#Dp_Palindrome_Partitioning.py

def is_palindrome(s,start,end):
	if start==end:
		return True
	elif end > start:
		if s[start]==s[end]:
			return True
		else:
			return False
	else:
		return True

s=input("enter the string: ")
dp=[]
dp.append([[]])

for i in range(len(s)):
	local=[]
	for j in range(i+1):
		start=j
		end=i
		if is_palindrome(s,start,end):
			for my_list in dp[j]:
				my_list=my_list.copy()
				my_list.append(s[start:end+1])
				local.append(my_list)
	dp.append(local)

print(dp[-1])
