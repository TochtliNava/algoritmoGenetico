class Cromosoma:

    def __init__(self):
        self.cromosomas = []
        self.fitness = []
        self.length = 0

    def setLength(self, l):
        self.length = l
    
    def getLength(self):
        return self.length
    
    def getSize(self):
        return len(self.cromosomas)

    def clearFitness(self):
        self.fitness.clear()

    def addFitness(self, f):
        self.fitness.append(self.getFitness(f))

    def clearCromosomas(self):
        self.cromosomas.clear()

    def addCromosoma(self, c):
        self.cromosomas.append(c)

    def getFitness(self, c):
        k, fit = 0, 0

        for i in range(len(c)):
            if(c[i] == "1"):
                k = k + 1
            else:
                if(k > fit):
                    fit = k
                k = 0

        if(k > fit):
            fit = k

        return fit
    
    def __str__(self) -> str:
        return f"{self.cromosomas}"

    def mutate(self):
        self.clearFitness()
        
        for i in range(self.getSize()):
            temp_cromosoma = ""
            for u in range(len(self.cromosomas[i])):
                if(self.cromosomas[i][u] == "1"):
                    temp_cromosoma = temp_cromosoma + "0"
                if(self.cromosomas[i][u] == "0"):
                    temp_cromosoma = temp_cromosoma + "1"
            self.cromosomas[i] = temp_cromosoma
            self.addFitness(self.cromosomas[i])
    
    def breed(self):
        for i in range(int(self.getSize()//2)):
            temp = self.cromosomas[i][int((self.getLength()//2)):]
            self.cromosomas[i] = self.cromosomas[i][:int(self.getLength()//2)] + self.cromosomas[(i + int(self.getSize()//2))][int(self.getLength()//2):]
            self.cromosomas[int(i + (self.getSize()//2))] = self.cromosomas[int(i + (self.getSize()//2))][:int((self.getLength()//2))] + temp

cromosoma = Cromosoma()