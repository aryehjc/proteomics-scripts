#!/usr/bin/python3

#Calculates Mass of N-Glycan.

import sys
print('Enter Total masses of protons, sodium ions, water, Hexose, HexNac, Fucose, NeuAc, NeuGc, RFMS.')

myList = list(map(float, input("Enter parameters: ").split(',')))

# As glycans have a range of +1 to +3 charge typically. Amend in webapp.
if myList[0] > 0 and myList[1] == 0:
    charge = myList[0] + myList[1]
    print('Charge is ' + str(round(myList[0] + myList[1])))
if 22.9898 <= myList[1] < 45.9796 and myList[0] == 0:
    charge = 1
    print('Charge is 1.')
if 45.9796 <= myList[1] < 68.9694 and myList[0] == 0:
    charge = 2
    print('Charge is 2.')
if 22.9898 <= myList[1] < 45.9796 and myList[0] == 1:
    charge = 2
    print('Charge is 2.')
if myList[1] >= 68.9694 and myList[0] == 0:
    charge = 3
    print('Charge is 3.')
if 22.9898 <= myList[1] < 45.9796 and myList[0] == 2:
    charge = 3
    print('Charge is 3.')
if 45.9796 <= myList[1] < 68.9694 and myList[0] == 1:
    charge = 3
    print('Charge is 3.')

for i in myList:
    print(i, end=' ')

numerator = (myList[0] + myList[1] + myList[2] + (3 * myList[3])
+ (2 * myList[4]) + myList[5] + myList[6] + myList[7] + myList[8]) / charge 
massofGlycan =  numerator / charge
# Can do sum(myList, 0) because format of sum is sum(iterable,start)
# This script sums totals unlike the other glycanmass one.

print('\nAre you sure?')
response = input()
if response == 'y':
    print('Glycan mass is : ' + str(massofGlycan))
elif response == 'n':
    sys.exit()
