#import matplotlib.pyplot as plt
#from pylab import plot, title, xlabel, ylabel, savefig, legend, array
def resultsExec():
    import matplotlib.pyplot as plt
    import statistics
    from server import distance
    f = open('estLoc.txt', 'r')
    final_res = open('final.txt', 'w')
    errFie = open('case4Err.txt', 'a+')
    realX = []
    realY = []
    estX = []
    estY = []
    err = []
    lines = f.readlines()
    count = 0
    fe = [[0],[0],[0],[0]]

    for i in range(0, 3000):
        x = lines[i].strip('\n').split(' ')
        
        if i == 0:
            fe=[ [float(x[0])] ,  [float(x[1])], [float(x[2])], [float(x[3])]]
        elif i < 50:
            fe[0].append(float(x[0]))
            fe[1].append(float(x[1]))
            fe[2].append(float(x[2]))
            fe[3].append(float(x[3]))       
        else:
            fe[0].append(float(x[0]))
            fe[1].append(float(x[1]))
            fe[2].append(float(x[2]))
            fe[3].append(float(x[3]))
            fe[0].pop(0)
            fe[1].pop(0)
            fe[2].pop(0)
            fe[3].pop(0)
        estX.append(round(statistics.mean(fe[0]),2))
        estY.append(round(statistics.mean(fe[1]),2))
        realX.append(round(statistics.mean(fe[2]),2))
        realY.append(round(statistics.mean(fe[3]),2))
        final_res.write(str(realX[i])+' '+ str(realY[i])+' '+str(estX[i])+' '+str(estY[i])+' '+'\n')
        err.append(round(distance((realX[i], realY[i]), (estX[i],estY[i])),2))

        
        count+=1
    print('reduced avarge error', round(statistics.mean(err), 2))

    #plt.scatter(realX,realY)
    #plt.scatter(estX,estY)
    plt.xlim(0, 50)
    plt.ylim(0,50)
    plt.xticks(range(0,50,5))
    plt.yticks(range(0,50,5))
    print(len(estX))
    plt.autoscale(False)
    plt.plot(realX,realY, label='Real path')
    plt.plot(estX,estY, '-', label = 'Estimated path')
    plt.legend()
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.plot(16.6, 16.6, markersize=4, color='red', marker='o', label = 'AP1')
    plt.plot(16.6, 33.3, markersize=4, color='red', marker='o', label = 'AP2')
    plt.plot(33.3, 16.6, markersize=4, color='red', marker='o', label = 'AP3')
    plt.plot(33.3, 33.3, markersize=4, color='red', marker='o', label = 'AP4')
    #plt.plot(estX,estY)
    errFie.write(str(round(statistics.mean(err),2)) + '\n')
    errFie.close()

