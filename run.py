from rogueAP import exec
from server import locate
from Crypto.Random import random

exec((random.randrange(1, 49), random.randrange(1, 49)), sigma = 2)
locate()
import results