# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rvxmAxcJGhzDywqO_kqq18Pv7vt8HAxV
"""

a=int(input("Enter the cost of 1st item: "))
b=int(input("Enter the cost of 2nd item: "))
c=int(input("Enter the cost of 3rd item: "))
total=a+b+c
if(total>50):
  total=total*0.9
  print("Total Cost: ", total)
else:
    print("No discount")