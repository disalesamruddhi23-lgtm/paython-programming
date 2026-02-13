# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 13:56:37 2026

@author: User
"""

n=int(input("enter number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("factorial:",fact)