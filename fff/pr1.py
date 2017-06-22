# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:29:51 2017

@author: marina
"""
##определяем длинну наименьшего слова в стоке
#s = input()
#w = 0
#min_w = len(s)
#for i in s:
#	if 'a'<=i<='z' or 'A'<=i<='Z' \
#	or 'а'<=i<='я' or 'А'<=i<='Я':
#		w += 1
#	else:
#		if w < min_w and w != 0:
#			min_w = w
#		w = 0
#min_w = w 
#print(min_w)

s,m = 0,1
for n in input('Enter number: '):
    s += int(n)
    m *= int(n)
print('Sum of digits =',s,'\nMultiplication of digits =',m)
























































