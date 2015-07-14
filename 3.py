import xlrd

data_xls=xlrd.open_workbook('1.xls')
table=data_xls.sheets()[0]

nrows=2530
f=file("feedback.txt",'w')
for i in range(1,nrows):
    if str(table.cell(i,31))[7:-1]=='no' and str(table.cell(i,32))[7:-1]=='no':
        print 'no',i
        f.write('no\n')
    else:
        f.write('yes\n')
f.close()
