'''
Created on Jul 9, 2014

@author: viejoemer

HowTo create a copy of a set in Python?

¿Cómo crear una copia de un juego en Python?
'''

#Create a set with values.
s = set([0,1,2,3])
print("set one", s)

#Never use set = set
s2 = s
print("'equal copy' set one", s2)

#If you clean the first set, this gonna clean the second one.
s.clear()
print("set one", s)
print("'equal copy' set one", s2)

s = set([0,1,2,3])
#The right way is {}.copy
s_copy = s.copy()
s.clear()
print("set one", s)
print("right copy set one", s_copy)