import queue

def readfile():

    processosLeitura = {}

    arq = open("entrada.txt")
    linhas = arq.readlines()
    for linha in linhas:
        partes = linha.strip().split()
        fila = queue.Queue()
        if len(partes) == 4:
            numeros = partes[3].split(",")
            for i in numeros:
                fila.put(int(i))
        processosLeitura[partes[0]] = [int(partes[1]), int(partes[2]),fila, int(0)]

    return dict(sorted(processosLeitura.items(), key=lambda item: item[1][1]))

# EXPLANATION
# ENTRADA:
# NOME(PROCESSO) | TEMPO(CPU/TOTAL) | TEMPO(CHEGADA) | I/O INTERRUPÇÃO(CPU/PARCIAL) [FILA]
# ---------------|------------------|----------------|----------------------------------
# P1             | 9                | 10             | 2, 4, 6, 8
# ---------------|------------------|----------------|----------------------------------
# P2             | 10               | 4              | 5
# ---------------|------------------|----------------|----------------------------------
# P3             | 5                | 0              | 2
#----------------|------------------|----------------|----------------------------------
# P4             | 7                | 1              | 3, 6
#----------------|------------------|----------------|----------------------------------
# P5             | 2                | 17             |

# processo:
# KEY:
#  (NOME | STRING)
# VALUE:
#   processo[0] (TEMPO/CPU | INT)
#   processo[1] (TEMPO/CHEGADA | INT)
#   processo[2] (I/O | FILA<INT>)
#   processo[3] (CONTADOR I/O | INT)
