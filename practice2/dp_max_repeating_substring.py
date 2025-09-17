#Dp_maxrepeatingsubstring.py

seq=input("enter the sequence:")
word=input("enter the word:")
DP=[-1 for _ in range(len(seq))]
count=0

#type1:bottomup
# i=len(word)-1
# while(i<len(seq)):
# 	j=i-(len(word)-1)
# 	print(seq[j:i+1],word)
# 	if seq[j:i+1]==word:
# 		DP[i]=1+DP[j-1]
# 		if DP[i]>count:
# 			count=DP[i]
# 	i+=1
# print(DP)
# print(count)

#type2:top down
def max_rep_substrings(seq,word,i,DP)->int:
	if DP[i]!=-1: 
		return DP[i]
	if i<len(word)-1:
		DP[i]=0 
		return DP[i]
	j=i-(len(word)-1)
	if seq[j:i+1]==word:
		print(i,j)
		DP[i]=1+max_rep_substrings(seq,word,j-1,DP) 
	else: 
		DP[i]=0
	return DP[i]


for i in range(len(seq)-1,-1,-1):
	max_rep_substrings(seq,word,i,DP)

print(DP)