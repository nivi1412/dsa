#encodebitstostring.py
#00:A 01:T 10:G 11:C

def decode():
	length=int(input("enter the length of message:"))
	message=input("enter the bits to be decode:")
	msg_len=len(message)
	result=""

	for i in range(0,msg_len,+2):
		if message[i:i+2]=="00":
			result+="A"
		elif message[i:i+2]=="01":
			result+="T"
		elif message[i:i+2]=="10":
			result+="G"
		elif message[i:i+2]=="11":
			result+="C"
	return result


testcase=int(input("enter number of testcases:"))

for i in range(testcase):
	result=decode()
	print(result)




