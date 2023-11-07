from importFile import readfile
from roundRobin import roundRobin

processos = readfile()

Quantum = 4

rr = roundRobin(processos, Quantum)

rr.start()

rr.plot()
