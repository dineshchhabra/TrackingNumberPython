records = []
new_records = []
records.append([1,'A',1])
records.append([2,'A',1])
records.append([6,'A',1])
records.append([10,'A',1])
records.append([15,'A',2])
records.append([20,'A',2])
 

idx = 0
end = 0
while idx < len(records):
    start = records[idx][0]
    status_code = records[idx][1]
    transfer_code = records[idx][2]

    idx = idx + 1
    pair = 1
    while idx < len(records) and records[idx][1] == status_code and records[idx][2] == transfer_code:
        if (pair != 1 and records[idx][0] != end + 1):
            break
        end = records[idx][0]
        pair = 0
        idx = idx + 1
        
    new_records.append([start, end, status_code, transfer_code])
       
print(new_records)
    
