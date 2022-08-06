#----------------------------------------------------------------------------------------------------------------------------
import math
#Math module imported
import time
#Time module imported
#----------------------------------------------------------------------------------------------------------------------------
print('What would you like to do with this calculator?')
time.sleep(0.5)
print('1. Addition')
time.sleep(0.5)
print('2. Substraction')
time.sleep(0.5)
print('3. Multiplition')
time.sleep(0.5)
print('4. Division')
time.sleep(0.5)
#----------------------------------------------------------------------------------------------------------------------------
calc = int(input('Enter Task : ')) 
x = int(input('Enter 1st number : '))
y = int(input('Enter 2nd number : '))
time.sleep(0.5)
print('Calculating your answer...')
time.sleep(0.5)
#----------------------------------------------------------------------------------------------------------------------------
if  calc ==1:
     print('The sum of %i and %i is %i' % (x, y, x+y))
elif calc ==2:
     print('The difference of %i and %i is %i' % (x, y, x-y))
elif calc ==3:
     print('The product of %i and %i is %i' % (x, y, x*y))
elif calc ==4:
     print('The division of %i and %i is %i' % (x, y, x/y))
else:
     print('Error')
#----------------------------------------------------------------------------------------------------------------------------
#Ending process command
end = input('Press Enter to kill process.')
print('Process Ended')
#----------------------------------------------------------------------------------------------------------------------------