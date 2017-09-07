# -*- coding: utf-8 -*-
import math as m
import numpy as np

n=150
i=0
x=1
a=0
while i<n:
	fac=1 
	k=0 
	while k<2*i:
		k=k+1
		fac=fac*k
	a+=((-1)**i)*(x**(2*i))/fac
	i=i+1
print(a)
print(m.cos(x))