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
            user = []
            add_rut = True

            while add_rut:
                try:
                    rut_user = input('A continuación, ingrese su rut sin puntos y con guión para grabar (ejemplo: 12345678-9) ->\n')
                    rut_validado = valida_rut(rut_user)

                    if rut_validado == True:
                        user.append(rut_user)
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
                    if respuesta_nombre_afiliado.isalpha():
                        if len(respuesta_nombre_afiliado) > 2:
                            user.append(respuesta_nombre_afiliado)
                        else:
                            print('Debe ingresar un Nombre válido.\n')
                    else:
                        print('Debe ingresar un Nombre (letras)!\n')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')

            add_apellido = True
            while add_apellido:
                try:
                    respuesta_apellido_afiliado = input('Ingrese su apellido Paterno ->\n')
                    if respuesta_apellido_afiliado.isalpha():
                        if len(respuesta_apellido_afiliado) > 2:
                            user.append(respuesta_apellido_afiliado)
                            add_apellido = False
                        else:
                            print('Debe ingresar un Apellido válido.\n')
                    else:
                        print('Debe ingresar un Apellido (letras)!\n')
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

                    try:
                        respuesta_pelicula = int(input('Ingrese el número según función que desee: -> '))
                        user.append(getNameDict(funciones_peliculas, respuesta_pelicula))
                        add_pelicula = False
                    except:
                        print('Ingresa una opción válida para las funciones disponibles!')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')
            
            add_funcion_horario = True
            while add_funcion_horario:
                try:
                    print('Selecciona un horario disponible:\n')
                    for nameItem, rsp in funciones_peliculas.items():
                        if rsp["respuesta"] == respuesta_pelicula:
                            for index, hora in enumerate(rsp["horarios"]):
                                print(f'{index + 1} - {hora}\n')

                    respuesta_horario = int(input('Ingrese el número según horario que desee: -> '))
                    try:
                        user.append(getHorarioFuncion(funciones_peliculas, respuesta_pelicula, respuesta_horario))
                        add_pelicula = False
                    except:
                        print('Ingresa una opción válida para el horario de la función.\n')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!\n')

            add_tipoEntrada = True
            while add_tipoEntrada:
                try:
                    print('Seleccione el tipo de entrada que desea comprar según el número indicado.\n Recuerde que solo puede comprar un máximo de 2 entradas ** ->\n ')
                    for index, item in enumerate(tickets_entradas):
                        if tickets_entradas[item]["estado"] == True:
                            print(
                                f'{index + 1} = {tickets_entradas[item]["nombre"]} - ${tickets_entradas[item]["valor"]}\n')

                    respuesta_ticket = int(input('Ingrese el número según el "Tipo de Ticket" que desee:\n -> '))
                    respuesta_cantidad_tickets = int(input('Ingrese el número entradas que desee: -> \n ** Solo puede comprar un máximo de 2 entradas y mínimo 1 **\n ->'))

                    orden_compra = []
                    if respuesta_cantidad_tickets == 1 or respuesta_cantidad_tickets == 2:
                        
                        orden_compra.append(getNameDict(tickets_entradas, respuesta_ticket))
                        orden_compra.append(respuesta_cantidad_tickets)
                        orden_compra.append(respuesta_cantidad_tickets * getValorDict(tickets_entradas, respuesta_ticket))

                        add_tipoEntrada = False
                    else:
                        print(f'Opción ingresada {respuesta_ticket} no es válida. Ingrese canitdad permitida!\n')

                    try:
                        print('A continuación, se presenta la disponibilidad de asientos.\n Considere el número de asiento para reservar. Los Marcados en "X" están reservados.\n')
                        asiento_reserva = []

                        resultado = np.array(render_asientos_usados(asientos_cine))
                        cine_matriz = resultado.reshape(5, 10)
                        while respuesta_cantidad_tickets != len(asiento_reserva):
                            pantalla = f'\t[*** PANTALLA CINE ***]\n {cine_matriz}'

                            try:
                                respuesta_asiento = int(input(f'Ingrese su asiento según Disposición ->\n {pantalla}\n Asiento -> '))
                                
                                reserva_asiento(asientos_cine, respuesta_asiento)
                                asiento_reserva.append(respuesta_asiento)

                                print(f'{pantalla}\n Asiento Nº {respuesta_asiento} reservado con éxito! \n')

                            except:
                                print('Ingrese un número de asiento Disponible! \n')
                        orden_compra.append(asiento_reserva)
                        user.append(orden_compra)
                        
                        print('Proceso de reserva completado con éxito!\n')

                    except:
                        print('Error en ingreso de entrada')

                except:
                    print(
                        'Verifique que los datos estén correctos o vuelva a intentarlo!')
                        
            add_confiteria = True

            while add_confiteria:
                try:
                    respuesta_confiteria = int(input('¿Desea agregar confitería?\n 1 = Si\n 2 = No\n'))
                    confiteria = []
                    if respuesta_confiteria == 1:
                        confiteria_palomitas = []
                        print('Esta es nuestra carta de Palomitas Disponibles: ->\n')
                        for index, item in enumerate(palomitas):
                            print(f'{index + 1} = {palomitas[item]["nombre"]} - ${palomitas[item]["valor"]}\n')
                        
                        #step!
                        respuesta_palomitas = int(input('Indique la opción según Palomitas que desees: -> '))

                        confiteria_palomitas.append(getNameDict(palomitas, respuesta_palomitas))
                        confiteria_palomitas.append(getValorDict(palomitas, respuesta_palomitas))
                        confiteria.append(confiteria_palomitas)
                        print('Palomitas agregadas correctamente! \n')

                        add_confiteria = False
                    else:
                        print('Gracias por preferirnos! Vuelva pronto!\n')
                        add_confiteria = False

                    user.append(confiteria)
                except:
                    print('Error en ingreso de Palomitas')
                        

        elif respuesta_menu == 4:
            print('Cerrando Sesión de Compras en CineHoy\n')
            estapa_menu = False

        else:
            print('Opción inválida, intente nuevamente o contacte al administrador.')

print(user)
print(users_bd)
