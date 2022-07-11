import numpy as np

x = [['18355317-8', 'Matias', 'Espinoza', [18, 19], 5000], ['11046220-4', 'Beatriz', 'Escobar', [22, 23], 5000]]

# lista = np.array(x)

for user in x:
    rut, nombre, apellido, asientos, valor_pago = user
    if rut == '18355317-8':
        print(asientos)

# number_list = [1, 2, 3, 4, 5]
# alpha_list = ['A', 'B', 'C', 'D', 'E']

# asientos = []
# for i in alpha_list:
#     for j in number_list:

#         asientos.append(i + str(j))

# lista = np.array(asientos)

# orden = lista.reshape(5, 5)

# reserva = np.char.replace(orden, 'A1', 'X')

# print(reserva)

# user = []
# add_nombre = True
# while add_nombre:
#     respuesta_nombre_afiliado = input('Ingrese su nombre ->\n')
#     if respuesta_nombre_afiliado.isalpha():
#         if len(respuesta_nombre_afiliado) > 2:
#             user.append(respuesta_nombre_afiliado)
#             add_nombre = False
#         else:
#             print('Debe ingresar un Nombre válido.\n')
#     else:
#         print('Debe ingresar un Nombre (letras)!\n')
