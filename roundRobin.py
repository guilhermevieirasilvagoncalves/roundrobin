import queue
import matplotlib.pyplot as plt

def getFila(processos):
    Fila = queue.Queue()

    for i in processos:
        Fila.put([i, processos[i][1]])

    return Fila

class roundRobin:
    
    def __init__(self, process, quantum):
        self.process = process
        self.quantum = quantum
        self.listProcess = {}
        self.processName = []

    def start(self):

        print("""
***********************************
***** ESCALONADOR ROUND ROBIN *****
-----------------------------------
------- INICIANDO SIMULACAO -------
-----------------------------------
    """)

        processQueue = getFila(self.process) # Fila de processos ainda não chamados
        processName = []
        timeProcess = 0 # <int> loop time
        newProcess = False
        IOProcess = False
        endProcess = False
        quitProcess = False
        quantumProcess = False
        item = ""
        novo = ""
        quantumP = ""
        
        Fila = queue.Queue() # Fila CPU

        Fila.put(processQueue.get()[0]) # Push primeiro fila de processos

        while(True): # Enquanto a Fila de CPU não esta vazia

            if(len(Fila.queue) == 0 and len(processQueue.queue) == 0):
                quitProcess = True
            else:
                QuantumCounter = self.quantum

                P = Fila.get() # Pegar o primeiro processo da Fila de CPU

                if P not in self.listProcess:
                    self.listProcess.setdefault(P, [[timeProcess], []])
                    self.processName.append(P) 
                else:
                    self.listProcess[P][0].append(timeProcess)

            while QuantumCounter > 0:

                print(f"********** TEMPO {timeProcess} **************")

                
                if(IOProcess):
                    print(f"#[evento] OPERACAO I/O <{item}>")
                    IOProcess = False
                if(quantumProcess):
                    print(f"#[evento] FIM QUANTUM <{quantumP}>")
                    quantumProcess = False
                if(newProcess):
                    print(f"#[evento] CHEGADA <{novo}>")
                    Fila.put(novo)
                    newProcess = False
                if(endProcess):
                    print(f"#[evento] ENCERRANDO <{item}>")
                    endProcess = False

                if(not len(Fila.queue)):
                    print("FILA: Nao ha processos na fila")
                    if(quitProcess):
                        break
                else:
                    print("FILA:", end=" ")
                    for i in range(len(Fila.queue)):
                        item = Fila.queue[i]
                        print(f"{item}({self.process[item][0]})", end=" ")
                    print()

                self.process[P][3] += 1

                timeProcess += 1
                
                processoAtual = self.process[P][0]
                
                print(f"CPU: {P}({processoAtual})")

                processoAtual -= 1

                if(len(processQueue.queue) and timeProcess == processQueue.queue[0][1]):
                    novo = processQueue.get()[0]
                    newProcess = True

                if(processoAtual == 0):
                    self.process[P][0] = 0
                    endProcess = True
                    item = P
                    self.listProcess[P][1].append(timeProcess)
                    break

                elif(len(self.process[P][2].queue) and len(self.process[P][2].queue) and self.process[P][2].queue[0] == self.process[P][3]):
                    self.process[P][2].get()
                    item = P
                    self.process[P][0] = processoAtual
                    Fila.put(P)
                    IOProcess = True

                    self.listProcess[P][1].append(timeProcess)
                    break
                else:
                    self.process[P][0] = processoAtual

                QuantumCounter -= 1
            
            if(QuantumCounter == 0):
                quantumP = P
                Fila.put(P)
                quantumProcess = True
                self.listProcess[P][1].append(timeProcess)

            if(quitProcess):
                print("ACABARAM OS PROCESSOS!!!")
                break

    def plot(self):
        # Define your project tasks with multiple time intervals for each task
        tasks = []
        for i in range(len(self.processName)):
            for j in range(len(self.listProcess[self.processName[i]][0])):
                tasks.append({
                "task": self.processName[i],
                "attributes": [
                    {"start": self.listProcess[self.processName[i]][0][j], "end": self.listProcess[self.processName[i]][1][j]}
                ]
            })

        def plot_gantt_chart(tasks):
            fig, ax = plt.subplots(figsize=(10, 5))
            color_mapping = {}
            tasks2 = sorted(tasks, key=lambda x: x['task'])
            for i, task in enumerate(tasks2):
                task_name = task["task"]
                
                attributes = task.get("attributes", [])
                
                if task_name not in color_mapping:
                    color_mapping[task_name] = f"C{i}"
                for interval in attributes:
                    start_date = interval["start"]
                    end_date = interval["end"]
                    duration = end_date - start_date

                    ax.barh(task_name, width=duration, left=start_date, height=0.3, align='center',color=color_mapping[task_name])

                    # Display additional attributes as labels
                    attribute_labels = "\n".join([f"Start: {start_date}", f"End: {end_date}"])
                    label = ax.text(start_date + duration / 2, task_name, attribute_labels, va='center', ha='center')
                    label.set_fontsize(6)  # Tamanho da fonte do texto do atributo
                    label.set_weight("bold")
                    label.set_color("white")
            
            ax.set_xlabel("Tempo")
            ax.set_ylabel("Processos")
            ax.set_title("Round Robin")
            plt.grid(False)
            plt.tight_layout()
            plt.show()

        plot_gantt_chart(tasks)