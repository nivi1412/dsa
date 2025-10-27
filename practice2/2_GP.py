# 2_GP.py

def GP(n,open_count,close_count,string,Ans):
	if len(string)==2*n:
		Ans.append(string)
	if open_count<n:
		GP(n,1+open_count,close_count,string+"(",Ans)
	if close_count<open_count:
		GP(n,open_count,1+close_count,string+")",Ans)

	return Ans


n=int(input("enter the paranthesis count: "))

print(GP(n,0,0,'',[]))