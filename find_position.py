import xlrd
import xlwt
import time
from faculty_scraper import searchName

def findPos(datafile, cols, newfilename):
     workbook1 = xlrd.open_workbook(datafile)
     worksheet = workbook1.sheet_by_index(0)
     book = xlwt.Workbook()
     sheet = book.add_sheet('Sheet_1', cell_overwrite_ok=True)
     row = 0
     while (worksheet.cell(row, 0).value !="END"):
        for j in range (0,cols):
            #print worksheet.cell(row, j).value
            sheet.write(row, j,worksheet.cell(row, j).value)

        if (worksheet.cell(row,1).value == xlrd.empty_cell.value):
            name = worksheet.cell(row,0).value
            if len(name)>20:
                name = name[0:20]
            dataList = searchName(name)
            time.sleep(0.2)
            if len(dataList)>0 and dataList[0].upper() == "DR":
                del dataList[0]
            if (len(dataList)>= 4):
                sheet.write(row, 1, dataList[-2])
                sheet.write(row, 2, dataList[-1])
            elif (len(dataList)==3):
                if (" " in dataList[0]):
                    sheet.write(row, 1, dataList[-2])
                    sheet.write(row, 2, dataList[-1])
                else:
                    sheet.write(row, 2, dataList[-1])
            elif (len(dataList)==2):
                sheet.write(row, 2, dataList[-1])

        row = row+1
     book.save(newfilename)
     print "done"

findPos("salaries_combined.xls", 9, "salary_test2.xls")
