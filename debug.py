import ipdb
from lib import *

c1 = Company("Spreetail", 2005)
c2 = Company("Schimiffels", 2010)
c3 = Company("TESTCOMPANY", 1999)

dev1 = Dev("Marcus M.")
dev2 = Dev("Scott H.")
dev3 = Dev("Bryn M.")

fb1 = Freebie(dev1, c1, "Pool Skimmer", 10)
fb2 = Freebie(dev1, c1, "Whistle", 5)
fb3 = Freebie(dev1, c2, "Mufflers", 150)
fb4 = Freebie(dev2, c1, "Skateboard", 100)
fb5 = Freebie(dev3, c3, "TEST", 15)
fb6 = Freebie(dev3, c1, "Pool", 2000)



ipdb.set_trace()