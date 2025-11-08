#palindromepartition.py
def partition(s):
	if len(s)==1:
		return [[s]]
	finallist=[]
	for i in range(1,len(s)):
		left=s[:i]
		right=s[i:]
		if left==left[::-1]:
			right_list=partition(right)
			for r in right_list:
				finallist.append([left]+r) 

	if s[::-1]==s: finallist.append([s])
	return finallist

s=input("enter the string: ")

print(partition(s))
