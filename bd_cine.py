from funciones_cine import getNameDict, getEstadoDict

tickets_entradas = {
    'entrada_estreno': {
        'nombre': 'Entrada Estreno',
        'valor': int(4800),
        'respuesta': 1
    },
    'entrada_normal': {
        'nombre': 'Entrada Normal',
        'valor': int(2900),
        'respuesta': 2
    }
}

funciones_peliculas = {
    '1': {
        'nombre': 'Spider - Man',
        'horarios': ['10:30 horas', '12:30 horas', '15:00 horas', '18:00 horas'],
        'estado': True,
        'respuesta': 1
    },
    '2': {
        'nombre': 'Avengers',
        'horarios': ['09:45 horas', '15:30 horas', '18:00 horas', '19:00 horas'],
        'estado': True,
        'respuesta': 2
    },
    '3': {
        'nombre': 'Animales Fantásticos',
        'horarios': ['11:00 horas', '13:30 horas', '16:00 horas', '19:00 horas'],
        'estado': True,
        'respuesta': 3
    }
}

palomitas = {
    'p_pequena': {
        'nombre': 'Palomitas Pequeñas',
        'valor': int(2500),
        'respuesta': 1
    },
    'p_mediana': {
        'nombre': 'Palomitas Medianas',
        'valor': int(4500),
        'respuesta': 2
    },
    'p_grande': {
        'nombre': 'Palomitas Grandes',
        'valor': int(7800),
        'respuesta': 3
    },
    'no': {
        'respuesta': 4,
        'valor': None
    }
}

bebidas = {
    'b_pequena': {
        'nombre': 'Bebida Pequeña',
        'valor': int(1000),
        'respuesta': 1
    },
    'b_mediana': {
        'nombre': 'Bebida Mediana',
        'valor': int(1250),
        'respuesta': 2
    },
    'b_grande': {
        'nombre': 'Bebida Grande',
        'valor': int(2000),
        'respuesta': 3
    },
    'no': {
        'respuesta': 4,
        'valor': None
    }
}

# for nameItem, rsp in funciones_peliculas.items():
#     print(nameItem)
#     for i in rsp["horarios"]:
#         print(i)

# def getHorarioFuncion(dict, respuesta):
#     for nameItem, rsp in dict.items():
#         if respuesta == int(nameItem):
#             for hora in rsp["horarios"]:
#                 return hora
    
  
  


# result = getHorarioFuncion(funciones_peliculas, 3)

# for index, item in enumerate(funciones_peliculas):

#     if funciones_peliculas[item]["estado"] == True:
#         print(f'{index + 1} = {funciones_peliculas[item]["nombre"]}')

# respuesta = int(input('Ingrese el número según película: -> '))
# for index, item in enumerate(funciones_peliculas):
#     if respuesta == funciones_peliculas[item]["respuesta"]:
#         print(f'Ud seleccionó:\n {funciones_peliculas[item]["nombre"]} {funciones_peliculas[item]["horarios"]}')


