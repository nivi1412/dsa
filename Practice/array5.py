# array5.py
# Given the position of a Bishop (A, B) on an 8 * 8 chessboard.
# Your task is to count the total number of squares that can be visited by the Bishop in one move.
# The position of the Bishop is denoted using row and column number of the chessboard.

# Input 1:
#  A = 4
#  B = 4
# Output 1:
#  13

A=int(input("enter the x cordinate of bishop:"))
B=int(input("enter the Y cordinate of bishop:"))
temp_A=A
temp_B=B
count=0

while(A>0 and B<7):
	count+=1
	A-=1
	B+=1
A=temp_A
B=temp_B


while(A>0 and B>0):
	count+=1
	A-=1
	B-=1
A=temp_A
B=temp_B


while(A<7 and B<7):
	count+=1
	A+=1
	B+=1
A=temp_A
B=temp_B


while(A<7 and B>0):
	count+=1
	A+=1
	B-=1	
print(count)
