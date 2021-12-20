class neuron:
    def __init__(self):
        self.inputs = [] ## 2d array input[[value,weight],[value,weight]]
        self.bias = -1


    def calcOutput(self):
        val = 0
        for i in range(0,len(self.inputs)):
            val = val + (self.inputs[i][0] * self.inputs[i][1])## getting all the input values 
        return val+self.bias


n1 = neuron()

n1.inputs.append([1,0.5])
n1.inputs.append([1,0.5])
n1.inputs.append([1,0.5])

print(n1.calcOutput())





