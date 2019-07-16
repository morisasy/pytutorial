"""
    created on june 17, 2019
    @author: Risasi
    pip install Xlsxwriter
    
"""

import xlsxwriter

mysheet = xlsxwriter.Workbook('mysheet.xlsx')
sheet = mysheet.add_worksheet() # sheet = mysheet.add_worksheet('names') 
sheet.write('A1', 'This is my sheet')
sheet.write('A2', "Eddy Rajabu")
mysheet.close()
