#note: clean up this mess after into soemthing reusable
import xlrd
import xlwt
workbook1 = xlrd.open_workbook('salaries-2013-14.xls')
worksheet = workbook1.sheet_by_index(0)
book = xlwt.Workbook()
sheet = book.add_sheet('Sheet_1', cell_overwrite_ok=True)

null = xlrd.empty_cell.value;
count = 1
endnum =0
while (count <10000):
    if (worksheet.cell(count,0).value=="END"):
        endnum = count
        count = 20000
        print "end of 2013 file"
        print endnum
    else:
        for j in range(0,5):
            sheet.write(count,j, worksheet.cell(count,j).value)
            #print worksheet.cell(count,j).value
        count = count +1
#for 2014 data TOTAL is the end of file, starts on row 7
workbook2 = xlrd.open_workbook('salaries-2014-15.xls')
sheet2 = workbook2.sheet_by_index(0)
def containsin2013(name):
    for i in range(1, endnum):
        if worksheet.cell(i,0).value==name:
            return "true"
    return "false"
count =1
added =0
while(sheet2.cell(count,0).value!= "TOTAL"):
    if (containsin2013(sheet2.cell(count,0).value)=="true"):
        for j in range(5,7):
            #print sheet2.cell(count, j-2).value
            sheet.write(count,j, sheet2.cell(count, j-2).value)
    else:
        added = added+1
        for j in range(0,3):
            sheet.write(added+endnum,j, sheet2.cell(count,j).value)
        for j in range(5,7):
            sheet.write(added+endnum,j, sheet2.cell( count, j-2).value)
    count = count+1
numrows = endnum+added
print numrows #the is the number of rows in the file after this part
print "end of 2014"


book.save('intermediate.xls')
