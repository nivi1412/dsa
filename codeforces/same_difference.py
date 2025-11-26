#same_difference.py
import math

test_case_count=int(input("enter the testcase count: "))
string_len=int(input("enter the string length: "))
string=input("enter the string: ")

letter_count_map={}
count=0

for i in range(len(string)-1):
	if string[i] != string[i+1]:
		string=string[:i]+string[i+1]+string[i+1:]
		print(string)
		count+=1

for letter in string:
	if letter not in letter_count_map:
		letter_count_map[letter]=0
	letter_count_map[letter]+=1

print(letter_count_map)
prev_val=-math.inf

for key,values in letter_count_map.items():
	if values>prev_val:
		prev_val=values

print(string_len-prev_val)
