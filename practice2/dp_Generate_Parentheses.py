# dp_Generate_Parentheses.py

def generateparenthesis(n,my_list,string,open_bracket,close_bracket):
	if len(string)==2*n:
		my_list.append(string)
	if open_bracket<n:
		generateparenthesis(n,my_list,string+"(",open_bracket+1,close_bracket)
	if close_bracket<open_bracket:
		generateparenthesis(n,my_list,string+")",open_bracket,close_bracket+1)


n=int(input("enter the count of parenthesis pair to be generated:"))

my_list=[]

generateparenthesis(n,my_list,"",0,0)

print(my_list)