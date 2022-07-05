import numpy as np
'''
class Matrix():
    def __init__(self, pos=(0,0), size=(10,5)):
        self.pos = pos
        self.matrix = np.empty(size, dtype='<U1')
        
        self.matrix[pos] = '🟢'
        
        for i in range(50):
            self.matrix[:,:] = i
    
    def __repr__(self):
        return self.matrix.__repr__()
    
    def __str__(self):
        return self.matrix.__str__()
    
    def change_pos(self, new):
        self.matrix[self.pos] = '⬛'
        self.matrix[new] = '🟢'
        self.pos = new
'''
cine_asientos = np.arange(1, 51, 1)

cine_matriz = cine_asientos.reshape(5, 10)

result = np.where(cine_matriz == 29)
listOfCoordinates= list(zip(result[0], result[1]))

for i in listOfCoordinates:
    row = i[0]
    column = i[1]

    cine_matriz[row][column] = -1

usados_asientos = []
for asientos in cine_matriz:
    for reserva in asientos:
        if reserva == -1:
            usados_asientos.append('X')
        else:
            usados_asientos.append(reserva)

print(usados_asientos)
