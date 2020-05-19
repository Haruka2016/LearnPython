#!/user/local/bin/python3
import csv
# with open('test1.csv','w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(['index','id','status','money'])
#     writer.writerows([[1,'aa',0,100],[2,'bb',1,200]])
# reader1 = {}

# import pandas as pd


with open('test.csv','r') as myself, open('test1.csv','r') as other, open('result.csv','w') as resultFile:
    reader1 = list(csv.DictReader(myself))
    reader2 = list(csv.DictReader(other))
    writer = csv.writer(resultFile)
    writer.writerow(['id','money','myStatus','otherStatus'])
    for myRecord in reader1:
        find = False
        for otherRecord in reader2:
            if otherRecord['id'] == myRecord['id']:
                find = True
                if myRecord['status'] != otherRecord['status']:
                    writer.writerow([myRecord['id'],myRecord['money'],myRecord['status'],otherRecord['status']])    
                del otherRecord
                break
        if not find:
            writer.writerow([myRecord['id'],myRecord['money'],myRecord['status'],'无记录'])

