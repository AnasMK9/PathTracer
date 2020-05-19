
import results, rogueAP,server
from Crypto.Random import random
for i in range(0, 50):
    rogueAP.exec((random.randrange(1, 49), random.randrange(1, 49)), sigma = 6)
    server.locate()
    results.resultsExec()

    print(i)