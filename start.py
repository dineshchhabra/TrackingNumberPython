print ("start of the program")
f=open('input.txt','r')
output=list()

for line in f:
	if line == "END"  or line == "0\n":
		print ()
	else:
		print (line)
		row=line.split(" ")
		print ("row is ",row)
		output.append(row)

print (output[0][0])
print (output)