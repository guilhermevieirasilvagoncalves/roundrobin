from importFile import readfile
from roundRobin import roundRobin

Quantum = 4
Quantum2 = 100000

# rr = roundRobin(Quantum)

# rr.readfile("entrada.txt")

# rr.start()

# rr.plot()

rrd = roundRobin(Quantum2)

rrd.readfile("entrada2.txt")

rrd.start()

rrd.plot()