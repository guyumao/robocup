import xlrd
import os
sent_dir=os.listdir('./data/sent')

email_list=[]
for i in sent_dir:
    current_dir='./data/sent/'+i
    current_dir_list=os.listdir(current_dir)
    for j in range(0,len(current_dir_list)):
        if current_dir_list[j][-4:]=='.pdf':
            current_dir_list[j]=current_dir_list[j][0:-4]
    for x in current_dir_list:
        email_list.append(x)

data_xls=xlrd.open_workbook('1.xls')
table=data_xls.sheets()[0]

nrows=2530
result=[0]

for i in range(nrows):
    result.append(0)

f=file('already_sent.txt','w')
for i in range(1,nrows):
    test_email=str(table.cell(i,4))[7:-1]
    print test_email
    if test_email in email_list:
        f.write('yes\n')
    else:
        f.write('no\n')
f.close()
