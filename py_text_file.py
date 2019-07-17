    """
    created on june 17, 2019
    @author: Risasi
    
"""

my_fp = open('myfile.txt', 'w')
try:
    my_fp.write('Hello india')

finally:
    my_fp.close()

with open('myfile.txt', 'w') as fp:
    fp.write('This is using with operator')
    
