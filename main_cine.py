import numpy as np
from funciones_cine import getNameDict, reserva_asiento, render_asientos_usados, valida_rut, getEstadoDict, getHorarioFuncion, getValorDict
from bd_cine import tickets_entradas, palomitas, bebidas, funciones_peliculas

users_bd = []
asientos_cine = np.arange(1, 51, 1)

estapa_menu = True

while estapa_menu:
    try:
        respuesta_menu = int(input(
            '*** Bienvenido a CineHoy ***\n 1.- Comprar Entradas\n 2.- Ver Asientos Disponibles\n 4.- Salir\n'))
    except:
        print('Ups! Opción inválida, vuelva a intentarlo.')
    else:
        if respuesta_menu == 1:
            user = {
                'rut': None,
                'nombre': None,
                'apellido': None,
                'orden_compra': {
                    'entradas': {
                        'pelicula': None,
                        'nombre_entrada': None,
                        'horario_funcion': None,
                        'cantidad_entrada': None,
                        'numero_asiento': [],
                        'valor': None
                    },
                    'confiteria': {
                        'acepta': False,
                        'palomitas': {
                            'nombre': None,
                            'valor': None,
                        },
                        'bebiba': {
                            'nombre': None,
                            'valor': None
                        }
                    },
                    'pago': {
                        'forma_de_pago': 'debito',
                        'valor_total': int(2500)
                    }
                }
            }
            add_rut = True

            while add_rut:
                try:
                    rut_user = input('A continuación, ingrese su rut sin puntos y con guión para grabar (ejemplo: 12345678-9) ->\n')
                    rut_validado = valida_rut(rut_user)

                    if rut_validado == True:
                        user["rut"] = rut_user
                        print('Rut Válido!\n')
                        add_rut = False
                    else:
                        print('RUT ingresado no es válido. Revise nuevamente el digito verificador!')
                except:
                    print('RUT inválido, revise o vuelva a intentarlo!\n')

            add_nombre = True

            while add_nombre:
                try:
                    respuesta_nombre_afiliado = input('Ingrese su nombre ->\n')
                    user["nombre"] = respuesta_nombre_afiliado

                    respuesta_apellido_afiliado = input('Ingrese su apellido Paterno ->\n')
                    user["apellido"] = respuesta_apellido_afiliado

                    add_nombre = False
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')

            add_pelicula = True

            while add_pelicula:
                try:
                    print(' *** Nuestra Cartelera disponible en CineHoy *** :\n Seleccione la opción según su número:\n')
                    for index, item in enumerate(funciones_peliculas):
                        if funciones_peliculas[item]["estado"] == True:
                            print(
                                f'{index + 1} = {funciones_peliculas[item]["nombre"]}\n')

                    respuesta_pelicula = int(input('Ingrese el número según función que desee: -> '))

                    user["orden_compra"]["entradas"]["pelicula"] = getNameDict(funciones_peliculas, respuesta_pelicula)

                    print('Selecciona un horario disponible:\n')
                    for nameItem, rsp in funciones_peliculas.items():
                        if rsp["respuesta"] == respuesta_pelicula:
                            for index, hora in enumerate(rsp["horarios"]):
                                print(f'{index + 1} - {hora}\n')

                    respuesta_horario = int(
                        input('Ingrese el número según horario que desee: -> '))

                    user["orden_compra"]["entradas"]["horario_funcion"] = getHorarioFuncion(
                        funciones_peliculas, respuesta_pelicula, respuesta_horario)

                    add_pelicula = False
                except:
                    print(
                        'Verifique que los datos estén correctos o vuelva a intentarlo!')

            add_tipoEntrada = True

            while add_tipoEntrada:
                try:
                    print('Seleccione el tipo de entrada que desea comprar según el número indicado.\n Recuerde que solo puede comprar un máximo de 2 entradas ** ->\n ')
                    for index, item in enumerate(tickets_entradas):
                        if tickets_entradas[item]["estado"] == True:
                            print(
                                f'{index + 1} = {tickets_entradas[item]["nombre"]} - ${tickets_entradas[item]["valor"]}\n')

                    respuesta_ticket = int(
                        input('Ingrese el número según el "Tipo de Ticket" que desee:\n -> '))
                    respuesta_cantidad_tickets = int(input(
                        'Ingrese el número según el ticket que desee: -> \n ** Solo puede comprar un máximo de 2 entradas y mínimo 1 **\n ->'))

                    if respuesta_cantidad_tickets == 1 or respuesta_cantidad_tickets == 2:
                        user["orden_compra"]["entradas"]["nombre_entrada"] = getNameDict(tickets_entradas, respuesta_ticket)
                        user["orden_compra"]["entradas"]["cantidad_entrada"] = respuesta_cantidad_tickets
                        user["orden_compra"]["entradas"]["valor"] = (respuesta_cantidad_tickets * getValorDict(tickets_entradas, respuesta_ticket))

                        add_tipoEntrada = False
                    else:
                        print(
                            f'Opción ingresada {respuesta_ticket} no es válida. Ingrese canitdad permitidas')

                    try:
                        print('A continuación, se presenta la disponibilidad de asientos.\n Considere el número de asiento para reservar. Los Marcados en "X" están reservados.\n')
                        user["orden_compra"]["entradas"]["numero_asiento"].clear()

                        resultado = np.array(render_asientos_usados(asientos_cine))
                        cine_matriz = resultado.reshape(5, 10)
                        while respuesta_cantidad_tickets != len(user["orden_compra"]["entradas"]["numero_asiento"]):
                            pantalla = f'\t[*** PANTALLA CINE ***]\n {cine_matriz}'

                            try:
                                respuesta_asiento = int(input(f'Ingrese su asiento según Disposición ->\n {pantalla}\n Asiento -> '))
                                
                                reserva_asiento(asientos_cine, respuesta_asiento)

                                user["orden_compra"]["entradas"]["numero_asiento"].append(respuesta_asiento)
                                print(f'{pantalla}\n Asiento Nº {respuesta_asiento} reservado con éxito! \n')
                            except:
                                print('Ingrese un número de asiento Disponible! \n')

                        users_bd.append(user)
                        print('Proceso de reserva completado con éxito!')

                    except:
                        print('Error en ingreso de entrada')

                except:
                    print(
                        'Verifique que los datos estén correctos o vuelva a intentarlo!')
                        
            add_confiteria = True

            while add_confiteria:
                try:
                    respuesta_confiteria = int(input('¿Desea agregar confitería?\n 1 = Si\n 2 = No\n'))

                    if respuesta_confiteria == 1:
                        user["orden_compra"]["confiteria"]["acepta"] = True

                        print('Esta es nuestra carta de Palomitas Disponibles: ->\n')
                        for index, item in enumerate(palomitas):
                            print(f'{index + 1} = {palomitas[item]["nombre"]} - ${palomitas[item]["valor"]}\n')
                        
                        #step!
                        respuesta_palomitas = int(input('Indique la opción según Palomitas que desees: -> '))

                        user["orden_compra"]["confiteria"]["palomitas"]["nombre"] = getNameDict(palomitas, respuesta_palomitas)
                        print('Palomitas agregadas correctamente! \n')

                        add_confiteria = False
                    else:
                        print('Gracias por preferirnos! Vuelva pronto!\n')
                        add_confiteria = False
                except:
                    print('Error en ingreso de Palomitas')
                        

        elif respuesta_menu == 4:
            print('Cerrando Sesión de Compras en CineHoy\n')
            estapa_menu = False

        else:
            print('Opción inválida, intente nuevamente o contacte al administrador.')

print(user)
print(users_bd)
