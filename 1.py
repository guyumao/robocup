import json
import xlrd

fp=open("test.json",'r')
str_data=fp.read()
data=json.loads(str_data[3:])
#file:json to dict

data_xls=xlrd.open_workbook('1.xls')
table=data_xls.sheets()[0]
#read table1

#nrows=table.nrows
nrows=2530 #the length of rows
result=[0]
for i in range(nrows):
    result.append(0)

for i in range(1,nrows):
    test_email=str(table.cell(i,4))[7:-1]
    #test_email=u'abancsaba@gmail.com'
    for number in data:
        if number['email']==test_email:
            print 'id=',number['id'],'row=',i,'email=',test_email
            print table.cell(i,3)
            result[i]=1

f=file('already_write.txt','w')
for i in range(1,nrows):
    print result[i]
    if result[i]==1:
        f.write('yes'+'\n')
    else:
        f.write('no'+'\n')
f.close()

