#DP_gen_paranthesis_backtracking.py

def genparan_backtack(n):
	result=[]
	def backtracking(current,open_count,close_count):
		print("current: ",current)
		if len(current)==2*n:
			result.append(current)
		if open_count<n:
			backtracking(current+"(",open_count+1,close_count)
		if close_count<open_count:
			backtracking(current+")",open_count,close_count+1)

	backtracking("",0,0)
	return result

n=int(input("enter the paranthesis count:"))
print(genparan_backtack(n))



