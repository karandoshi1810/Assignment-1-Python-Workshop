# -*- coding: utf-8 -*-
"""Assignment-1 Practical-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u60LVyiWxW_3lAiwL59oOU8BM7syr55S
"""

#Practical-1: There are two Input files are available to you named Input1.txt and Input2.txt.
#Read content from both files write in file Output.txt

#Writing values in file
file1 = open("Input1.txt","w")
file2 = open("Input2.txt","w")
file1.write("ABCD\nEDG\nF\nRT\n")
file2.write("PQR\nXYZ\n")
#Closing Files
file1.close()
file2.close()

#Opening output file ain apprnd mode and Input1 and Input2 in read mode
file3 = open("Output.txt","a")
file1 = open("Input1.txt","r")
file2 = open("Input2.txt","r")
#copying data from Input1 and Input2
f1_output = file1.read()
f2_output = file2.read()
#Writing data in Output
file3.write(f1_output)
file3.write(f2_output)
#Closing all files
file1.close()
file2.close()
file3.close()