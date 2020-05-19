#simulate the movement of the rogue AP and recieved RSSI values at the stationary
#APs based on the lognormal shadowing model
#Results will be written in a file to be read by the server to calculate the distance to the rogue AP
#Prx(d) = Prx(d0)-10*n*log(d/d0) + x(0, σ)
#rogue AP moves at a constant speed = 1m/sec
from time import sleep
from Crypto.Random import random
import math
from numpy import random as ff

AP1 = (16.6, 16.6)
AP2 = (16.6, 33.3)
AP3 = (33.3, 16.6)
AP4 = (33.3, 33.3)
#Rogue_loc = (random.randrange(1, 49), random.randrange(1, 49)) #initial location of the rogue AP

def distance(a, b):
    return round(math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2), 2)
    
def calcRSSI(AP, sigma, Rogue_loc):
    if(AP == 1):
        d = distance(AP1, Rogue_loc)
    elif(AP == 2):
        d = distance(AP2, Rogue_loc)
    elif(AP == 3):
        d = distance(AP3, Rogue_loc)
    elif(AP == 4):
        d = distance(AP4, Rogue_loc)
    else:
        print('Hmmm, did someone edit my code?')
        return 0
    if sigma == 0:
        return(round(-40 -10*3*math.log10(d/1),2 ))
    else:
        return(round(-40 -10*3*math.log10(d/1)+ff.normal(0,sigma,1)[0],2 ))

def calcDistance(RSSI):
    return(round(10**(-(RSSI+40)/30),2))


def exec(Rogue_loc,  sigma):
    f = open('simulation.txt', 'w')
    direction = random.choice([0, 1, 2, 3]) #movement direction, 0=up, 1=right, 2=down, 3=left
    step = 20 #change direction every x seconds
    speed = 1 #m/s
    '''stdev = input('please choose environment:\n 1:static\n2:semistatic\n3:somewhat dynamic\n4:highly dynamic\n')
    if stdev == '1':
        sigma = 0
    elif stdev == '2':
        sigma = 2
    elif stdev =='3':
        sigma = 4
    elif stdev == '4':
        sigma = 6'''
    
    for i in range(0,300): #each second
        for x in range(0, 10): #10 beacons/sec
            if direction == 0 and Rogue_loc[0] != 0:
                Rogue_loc = (round(Rogue_loc[0],2), round(Rogue_loc[1]+speed/10,2)) #move up
            elif direction == 1:
                Rogue_loc = (round(Rogue_loc[0]+speed/10, 2), round(Rogue_loc[1], 2)) #move right
            elif direction == 2:
                Rogue_loc = (round(Rogue_loc[0], 2), round(Rogue_loc[1]-speed/10,2)) #move down
            elif direction == 3:
                Rogue_loc = (round(Rogue_loc[0]-speed/10, 2), round(Rogue_loc[1], 2)) #move left

            if Rogue_loc[0] == 0 or Rogue_loc[0] == 50 or Rogue_loc[1]  == 0 or Rogue_loc[1] == 50: #correct movement direction in case it goes out of 50*50 range
                direction = (direction + 2) % 4
            
            f.write(str(Rogue_loc[0])+' '+str(Rogue_loc[1])+' '+str(calcRSSI(1, sigma,Rogue_loc))+' '+str(calcRSSI(2, sigma,Rogue_loc))+' '+str(calcRSSI(3, sigma,Rogue_loc))+' '+ str(calcRSSI(4, sigma,Rogue_loc))+'\n')

            '''    
            print('Distance from AP1 ', calcDistance(calcRSSI(distance(Rogue_loc, AP1))), 'real distance = ', distance(Rogue_loc, AP1))
            print('Distance from AP2 ', calcDistance(calcRSSI(distance(Rogue_loc, AP2))), 'real distance = ', distance(Rogue_loc, AP2))
            print('Distance from AP3 ', calcDistance(calcRSSI(distance(Rogue_loc, AP3))), 'real distance = ', distance(Rogue_loc, AP3))
            print('Distance from AP4 ', calcDistance(calcRSSI(distance(Rogue_loc, AP4))), 'real distance = ', distance(Rogue_loc, AP4))
            print(Rogue_loc)
        print(direction)'''
            
        if i % random.randrange(10, 25) == 0: #change direction at random intervals
            direction = random.choice([0, 1, 2, 3])
    f.close()
