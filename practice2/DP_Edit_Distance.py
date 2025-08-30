#DP_Edit_Distance.py

#for base case y do i have to check for all the cases onlyt for word1[0] and word2[0] is enough since 
#only first latters mush be delted or replaced or inserted at first position

#start main loop with 1,1
#base case check if single char is present in entire string , if present pass the i as dp value else 1+i
#base case lo direct ga chei dp[0][0] ni dp[1][0] lani dp[0][1] ki kaani vaadali anukoku ni tala kottukoku
#main recursion logic lo prev dp values vadaali kabatii akkada tala kottuko
#so base case lo dp[i][0]=i idi simple nu dp[i][0]=dp[0][0] eg: word1=rrrr word2=r 1 st case lo dp[0][0] anedi 0 vuntadi next anni 0 vastai but we have 
#to delete all the other r's so using i is correct.

word1=input("enter the word1: ")
word2=input("enter the word2: ")

dp=[[0 for _ in range(len(word2))]for _ in range(len(word1))]

dp[0][0]=0 if word1[0]==word2[0] else 1

for i in range(1,len(word1)):
	if word2[0] in word1[:i+1]:
		dp[i][0]=i
	else:
		dp[i][0]=i+1

for j in range(1,len(word2)):
	if word1[0] in word2[:j+1]:
		dp[0][j]=j
	else:
		dp[0][j]=j+1


print(dp)
for i in range(1,len(word1)):
	for j in range(1,len(word2)):
		dp[i][j]= 1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) if word1[i]!=word2[j] else dp[i-1][j-1]

print(dp)
print(dp[len(word1)-1][len(word2)-1])