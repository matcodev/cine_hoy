import numpy as np

usados_asientos = []
asientos_cine = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, -1], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]
asientos_cine_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, -1, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, -1, 37, 38, 39, 40, 41, 42, 43, 44, -1, 46, 47, 48, 49, 50]

list = np.arange(1, 51, 1)

for i in asientos_cine_b:
    if i == -1:
        usados_asientos.append('X')
    else:
        usados_asientos.append(i)

# print(usados_asientos)

cine_format = np.array(list)
cine_matriz_format = cine_format.reshape(5, 10)

index_asiento = asientos_cine_b.index(21)

index_list = cine_format.tolist().index(1)
# print(index_list)

for j in list:
    print(j)

