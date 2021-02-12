'''
02/11/2021

Review

Boolean Operators

not
and
or

Random Number Generator

import random (importing random library)
variable = random.randint(start, end)

======================================================================

while (Condition):
  BODY

else:
  BODY

#Ex
integer = 1

while (integer < 10):
  print ("This statement prints forever.")
  integer += 1  # incrementation
else:
  print ("This is the end of the while loop")  
'''

'''
Exercise 1
Expected outputs
  hello.  0
  Python. 1
  Python. 2
  Evergreen. 3
  Evergreen. 4
  Evergreen. 5
  2021. 6

student = 0

while (student <= 6):
  if (student < 1):
    print ("hello")
  elif (student < 3):
    print ("Python")
  elif (student < 3):
    print ("bye")
  elif (student <= 5):
    print ("Evergreen")
  else:
    print ("2021")

  student += 1


Exercise 2
Expected outputs
  hello 5
  Python 6
  Python 7 
  bye 8
  Evergreen 9
  Evergreen 10
  2021 11
'''
student = 5

while (student <= 11):
  if (student < 6):
    print ("hello")
  elif (student <= 7):
    print ("Python")
  elif (student <= 8):
    print ("bye")
  elif (student < 11):
    print ("Evergreen")
  else:
    print ("2021")

  student += 1







