# Program extracting all columns
# name in Python
import openpyxl

# Give the location of the file
loc = ("produceSales.xlsx")
 
# To load entire Workbook
wb = openpyxl.load_workbook(loc)

# Load one worksheet.
ws = wb['Sheet1']
all_rows = list(ws.rows)

# List all the sheets in the file.
#print("Found the following worksheets:")
#for sheetname in wb.sheetnames:
#    print(sheetname)


#print the first few rows of data:
#print(f"Found {len(all_rows)} rows of data.")
#print("\nFirst rows of data:")
#for row in all_rows[:500]:
#    print(row)

#Read the data in the rows
for cell in all_rows[1]:
    print(cell.value)