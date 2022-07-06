from funciones_cine import getNameDict, getEstadoDict

tickets_entradas = {
    'entrada_estreno': {
        'nombre': 'Entrada Estreno',
        'valor': int(4800),
        'respuesta': 1,
        'estado': True
    },
    'entrada_normal': {
        'nombre': 'Entrada Normal',
        'valor': int(2900),
        'respuesta': 2,
        'estado': True
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
        'respuesta': 1,
        'estado' : True
    },
    'p_mediana': {
        'nombre': 'Palomitas Medianas',
        'valor': int(4500),
        'respuesta': 2,
        'estado' : True
    },
    'p_grande': {
        'nombre': 'Palomitas Grandes',
        'valor': int(7800),
        'respuesta': 3,
        'estado' : True
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
#     if rsp["respuesta"] == 1:
#         for index, hora in enumerate(rsp["horarios"]):
#             print(index + 1, hora)


# for nameItem, rsp in funciones_peliculas.items():
#     for index, i in enumerate(rsp["horarios"]):
#         ''
    # print(index + 1 , i)

# def getHorarioFuncion(dict, respuesta, respuestaHorario):
#     for nameItem, rsp in dict.items():
#             if respuesta == rsp["respuesta"]:
#                 return rsp["horarios"][respuestaHorario - 1]
                    

# for nameItem, rsp in funciones_peliculas.items():
#         if 1 == rsp["respuesta"]:
#             for index, hora in enumerate(rsp["horarios"]):
#                 print(index, hora)
#                 print(rsp["horarios"][0])

# result = getHorarioFuncion(funciones_peliculas, 3, 2)

# print(result)
