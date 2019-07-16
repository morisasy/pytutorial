"""
    created on june 17, 2019
    @author: Risasi
    pip install Xlsxwriter
    
"""

import xlsxwriter

mysheet = xlsxwriter.Workbook('test.xlsx')
sheet = mysheet.add_worksheet() # sheet = mysheet.add_worksheet('names') 
sheet.write('A1', 'This is my sheet')
sheet.write('B1', "Eddy Rajabu")
sheet.write('C1', 'This is my sheet')
sheet.write('A2', "Zuhura")
sheet.write('B2', "Salama")
sheet.write('C2', "Salome")
mysheet.close()
