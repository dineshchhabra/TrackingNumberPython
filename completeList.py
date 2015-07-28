f=open('input.txt','r')
output={x: '-' for x in (range(1,120))}
for line in f:
	if line == "END"  or line == "0\n":
		print ()
	else:
		row=line.split(" ")
		for i in range(int(row[0]),int(row[1])+1) :
				output[i]=row[2]+""+row[3]

initial=1
curr=output[1]
for key,value in output.items():
	
	if curr is value:
		curr = value
		initial=key
	else: 
		print(str(initial)+" "+curr)
		curr=""
		initial=0
		
		