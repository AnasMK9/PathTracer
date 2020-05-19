import localization as lx
import numpy, math
import random
import sys
import os
import statistics
def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    
def calcDistance(RSSI):
    return(round(10**(-(RSSI+40)/30),2))


def locate():
    #location of access points
    AP1 = ['AP1', (16.6, 16.6)]
    AP2 = ['AP2', (16.6, 33.3)]
    AP3 = ['AP3', (33.3, 16.6)]
    AP4 = ['AP4', (33.3, 33.3)]
    #do the file thing
    res = open('estLoc.txt', 'w')
    i=1
    f =  open('simulation.txt', 'r')
    z = f.readlines()
    err = []
    fe = [[0],[0],[0],[0]]
    for i in range(0,3000):
        p  = lx.Project('2D','LSE')
        #set access points as anchors to use for localization
        p.add_anchor(AP1[0], AP1[1])
        p.add_anchor(AP2[0], AP2[1])
        p.add_anchor(AP3[0], AP3[1])
        p.add_anchor(AP4[0], AP4[1])
        #define target to locate
        rogue,label = p.add_target()
        x = z[i].strip('\n').split(' ')
        #fe=[(float(x[2])+fe[0]*(i+1))/(i+1), (float(x[3])+fe[1]*(i+1))/(i+1), (float(x[4])+fe[2]*(i+1))/(i+1), (float(x[5])+fe[3]*(i+1))/(i+1)]
        
        #print(x)
        if i == 0:
            fe=[ [float(x[2])],  [float(x[3])], [float(x[4])], [float(x[5])]]
            rogue.add_measure(AP1[0], calcDistance(fe[0][0]))
            rogue.add_measure(AP2[0], calcDistance(fe[1][0]))
            rogue.add_measure(AP3[0], calcDistance(fe[2][0]))
            rogue.add_measure(AP4[0], calcDistance(fe[3][0]))
        elif i < 5:
            fe[0].append(float(x[2]))
            fe[1].append(float(x[3]))
            fe[2].append(float(x[4]))
            fe[3].append(float(x[5]))
            rogue.add_measure(AP1[0], calcDistance(statistics.mean(fe[0])))
            rogue.add_measure(AP2[0], calcDistance(statistics.mean(fe[1])))
            rogue.add_measure(AP3[0], calcDistance(statistics.mean(fe[2])))
            rogue.add_measure(AP4[0], calcDistance(statistics.mean(fe[3])))
        else:
            fe[0].append(float(x[2]))
            fe[1].append(float(x[3]))
            fe[2].append(float(x[4]))
            fe[3].append(float(x[5]))
            fe[0].pop(0)
            fe[1].pop(0)
            fe[2].pop(0)
            fe[3].pop(0)
            rogue.add_measure(AP1[0], calcDistance(statistics.mean(fe[0])))
            rogue.add_measure(AP2[0], calcDistance(statistics.mean(fe[1])))
            rogue.add_measure(AP3[0], calcDistance(statistics.mean(fe[2])))
            rogue.add_measure(AP4[0], calcDistance(statistics.mean(fe[3])))

        #perform a multilateration to locate AP
        sys.stdout = open(os.devnull, "w")
        p.solve()
        sys.stdout = sys.__stdout__
        #just data types manipulation
        ltemp = tuple(map(lambda x: isinstance(x, float) and round(x, 1) or x, eval(str(rogue.loc).strip('p'))))
        #ltemp = tuple(str(rogue.loc).strip('p').strip())
        loc= (ltemp[0], ltemp[1])
        '''lt = (str(rogue.loc).strip('p').strip('(').strip(')').split(','))
        ltemp = (round(float(lt[0]),2),round(float(lt[1]),2))'''
        res.write(str(loc[0])+' '+str(loc[1])+' '+str(x[0])+' '+str(x[1])+'\n')
        est = (float(loc[0]),float(loc[1]))
        real=(float(x[0]), float( x[1]))
        err.append(round(distance(real,est),2))
        #print(i,'-','real location is ', real, 'init. estimated location is', loc, 'error is', round(distance(real,est),2), len(fe[0]))
        i = i+1
    print('avarge error', round(statistics.mean(err),2))
    f.close()
    res.close()
            



'''




#set access points as anchors to use for localization
p.add_anchor(AP1[0], AP1[1])
p.add_anchor(AP2[0], AP2[1])
p.add_anchor(AP3[0], AP3[1])
p.add_anchor(AP4[0], AP4[1])
R = (22,15)

for i in range(0, 50):
    rogue,label = p.add_target()
    rogue.add_measure(AP1[0], distance(R, AP1[1]))
    rogue.add_measure(AP2[0], distance(R, AP2[1]))
    rogue.add_measure(AP3[0], distance(R, AP3[1]))
    rogue.add_measure(AP4[0], distance(R, AP4[1]))
    sys.stdout = open(os.devnull, "w")
    p.solve()
    sys.stdout = sys.__stdout__
    
    ltemp = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, eval(str(rogue.loc).strip('p'))))
    loc= (ltemp[0], ltemp[1])

    print("estimated location =", loc)
    
    if random.choice([0, 1]) != 1:
        R = (R[0] + random.choice([1,-1])[0], R[1] ) # numpy.random.normal(0, 3, 1)[0] 
    else:
        R = (R[0], R[1] + random.choice([1,-1])[0]) #numpy.random.normal(0, 3, 1)[0]
    print('New location for R = ', R)
    '''