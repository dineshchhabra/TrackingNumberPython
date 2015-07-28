print ("start of the program")
f=open('input.txt','r')
trackrecords=[]


number = [];

def minNearest(trackNumber):
        pos = 0
        for ele in number:
                if ele[0] < trackNumber:
                        pos = ele[0]
        return pos;                

def maxNearest(trackNumber):
        pos = 1000
        for ele in number:
                if ele[0] > trackNumber:
                        return int(ele[0]);
        return(-1);        
        

def getRecord(trackNumber):
        for ele in number:
                if ele[0] == trackNumber:
                        return ele;
        


def updateTrackData(records):
     nearMax = 0   
     print(trackrecords)
     for record in records:
             nearMax = maxNearest(int(record[0]))
             
             print (nearMax)
             if record[0] not in number:
                     if nearMax == -1 :
                             number.append([int(record[0]),record[1],record[2]])
                             number.append([int(record[1]),record[1],record[2]])
                     if nearMax > int(record[0]):
                             nearMaxRecord= getRecord(nearMax);
                             number.append([int(record[0])-1,nearMaxRecord[1],nearMaxRecord[2]])
                             number.append([int(record[0]),record[1],record[2]])
                             if nearMax > int(record[1]):       
                                     number.append([int(record[1]),record[1],record[2]])
                                     number.append([int(record[1])+1,nearMaxRecord[1],nearMaxRecord[2]])
                                     print(nearMax)
                     
                     
                     
             number.sort(key=lambda x:x[0]);       
     return;


for line in f:
	if line == "END"  or line == "0\n":
		print ()
	else:
		print (line)
		row=line.split(" ")
		trackrecords.append(row)


updateTrackData(trackrecords)
print(number)
