#files must be xls to use
#END must be used at the end of column 0 to indicate an end to the data
#this does not have headers, they must be manually added

import xlrd
import xlwt

def appendFile (file1, f1cols, file2, f2cols, combined):
    workbook1 = xlrd.open_workbook(file1)
    worksheet = workbook1.sheet_by_index(0)
    book = xlwt.Workbook()
    sheet = book.add_sheet('Sheet_1', cell_overwrite_ok=True)
    empty_cell = xlrd.empty_cell.value
    spacernum = 2+ (f1cols-f2cols)
    #copying file 1 contents into the combined file
    row =0
    while (worksheet.cell(row, 0).value != ""):
        if worksheet.cell(row, 0).value == "END":
            break
        else:
            for j in range (0,f1cols):
                #print worksheet.cell(row, j).value
                sheet.write(row, j,worksheet.cell(row, j).value)
        row = row+1
    def lineOfWord(word):
         for i in range(0, row):
            cellvalue = worksheet.cell(i,0).value
            if (cellvalue == word or cellvalue in word or word in cellvalue):
                return i
        return -1000
    workbook2 = xlrd.open_workbook(file2)
    sheet2 = workbook2.sheet_by_index(0)
    count = 0
    added = 0
    while (sheet2.cell(count,0).value!="END"):
        location = lineOfWord(sheet2.cell(count,0).value)
        if (location >=0):
            for j in range(f1cols,f1cols+2):
                sheet.write(location, j, sheet2.cell(count,j-spacernum).value)
        else:
            for j in range(0, f2cols-2):
                sheet.write(added+row, j, sheet2.cell(count, j).value)
            for j in range(f1cols, f1cols+2):
                sheet.write(added+row,j, sheet2.cell( count, j-spacernum).value)
            added = added+1
        count = count+1
    sheet.write(added+row,0, "END")
    book.save(combined)
    print "done combining"




appendFile("salaries-2013-14.xls",5, "salaries-2014-15.xls", 5, "combined.xls")
appendFile("combined.xls", 7, "salary1516.xls", 6, "salaries_combined.xls")
