global cromosoma

class Cromosoma:

    def __init__(self):
        self.cromosomas = []
        self.fitness = []

    def clearFitness(self):
        self.fitness.clear()

    def addFitness(self, f):
        self.fitness.append(f)

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

cromosoma = Cromosoma()