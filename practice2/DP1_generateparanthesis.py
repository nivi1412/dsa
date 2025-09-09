# DP1_generateparanthesis.py

def gen_paran(n):
	result=[]
	def backtaracking(current,open_count,close_count):
		if len(current)==2*n:
			result.append(current)
		if open_count<n:
			backtaracking(current+"(",open_count+1,close_count)
		if close_count<open_count:
			backtaracking(current+")",open_count,close_count+1)
	backtaracking("",0,0)
	return result


n=int(input("enter the parathesis pair count: "))

print(gen_paran(n))