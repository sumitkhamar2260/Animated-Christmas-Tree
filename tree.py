#os.system('cls||clear')
from random import randint
from time import sleep
import os
rs=randint(1,30)

def gentree():
    #print('\033c')
    os.system('cls||clear')
    
    for x in range(1,30,2):
        rs1=randint(1,rs)
        if x==1:
            ch="$"
        elif rs1%4==0:
            ch="o"
        elif rs1%3==0:
            ch="i"
        else:
            ch="*"
        print("{:^33}".format(ch*x))
    print("{:^33}".format("|||"))
    print("{:^33}".format("|||"))
    sleep(.75)
while True:
   gentree()

print("Merry Christmas in Advance")
