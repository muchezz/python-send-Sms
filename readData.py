# Program extracting all columns
# name in Python
import openpyxl
import datetime

# Give the location of the file
loc = ("mwFellowship.xlsx")
 
# To load entire Workbook
wb = openpyxl.load_workbook(loc, data_only=True)

# Load one worksheet.
ws = wb['Sheet1']
all_rows = list(ws.rows)
#all_colm = list(ws.columns)

# List all the sheets in the file.
#print("Found the following worksheets:")
#for sheetname in wb.sheetnames:
#    print(sheetname)


#print the first few rows of data:
#print(f"Found {len(all_rows)} rows of data.")
#print("\nFirst rows of data:")
#for row in all_rows[:500]:
#    print(row)

# Generating Week Numbers
myDate = datetime.date.today()
year, week_num, day_of_week = myDate.isocalendar()
#print("This is week # " +str(week_num) + " Date " +str(day_of_week))

#Read the data in the rows
sheetWeekNo = []
for row in ws.rows:
    sheetWeekNo.append (row[0].value)
    #print(row[0].value)
    

for i in sheetWeekNo: 
    if(i == week_num) : 
        print ("Element Exists") 
    


