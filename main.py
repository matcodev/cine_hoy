import numpy as np

# x = [['18355317-8', 'Matias', 'Espinoza', 18, 19, 5000], ['11046220-4', 'Beatriz', 'Escobar', 22, 23, 5000]]

# lista = np.array(x)

# for user in lista:
#     rut, nombre, apellido, asiento_1, asiento_2, valor_pago = user
#     index = np.where(rut == '11046220-4')

#     listIndex = list(zip(index[0]))

#     print(listIndex)

number_list = [1, 2, 3, 4, 5]
alpha_list = ['A', 'B', 'C', 'D', 'E']

asientos = []
for i in alpha_list:
    for j in number_list:
    
        asientos.append(i + str(j)) 
        
lista = np.array(asientos)

orden = lista.reshape(5, 5)

reserva = np.char.replace(orden, 'A1', 'X')

print(reserva)