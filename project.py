radius = float(input("radius of circle:"))
print("area of circle is:", radius*radius*2.14)

import os.path

split_tub = os.path.splitext('sayyam.py')

file_name = split_tub[0]
file_extention = split_tub[1]
print("the file name is:",file_name)
print("the file extention is:", file_extention)