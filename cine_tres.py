import numpy as np
from funciones_cine import getNameDict, reserva_asiento, render_asientos_usados, valida_rut, getEstadoDict, getHorarioFuncion
from user import users_bd, user
from bd_cine import tickets_entradas, palomitas, bebidas, funciones_peliculas

asientos_cine = np.arange(1, 51, 1)

estapa_menu = True

while estapa_menu:
    try:
        respuesta_menu = int(input('*** Bienvenido a CineHoy ***\n 1.- Comprar Entradas\n 2.- Ver Asientos Disponibles\n 4.- Salir\n'))
    except:
        print('Ups! Opción inválida, vuelva a intentarlo.')
    else:
        if respuesta_menu == 1:
            add_rut = True

            while add_rut:
                try:
                    rut_user = input('A continuación, ingrese su rut sin puntos y con guión para grabar (ejemplo: 12345678-9) ->\n')
                    rut_validado = valida_rut(rut_user)

                    if rut_validado == True:
                        user["rut"] = rut_user
                        print('Rut Valido!\n')
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
                    print('Nuestra Cartelera disponible en CineHoy:\n Seleccione la opción según su número:\n')
                    for index, item in enumerate(funciones_peliculas):
                        if funciones_peliculas[item]["estado"] == True:
                            print(f'{index + 1} = {funciones_peliculas[item]["nombre"]}\n')
                    
                    respuesta_pelicula = int(input('Ingrese el número según función que desee: -> '))

                    user["orden_compra"]["entradas"]["pelicula"] = getNameDict(funciones_peliculas, respuesta_pelicula)

                    print('Selecciona un horario disponible:\n')
                    for index, item in enumerate(funciones_peliculas):
                        if funciones_peliculas[item]["estado"] == True:
                            print(f'{index + 1} = {funciones_peliculas[item]["horarios"][index]}\n')

                    respuesta_horario = int(input('Ingrese el número según función que desee: -> '))

                    user["orden_compra"]["entradas"]["horario_funcion"] = getHorarioFuncion(funciones_peliculas, respuesta_horario)

                    
                    add_pelicula = False
                    
                    respuesta_cantidad_entradas = int(input(''))
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')
                


        elif respuesta_menu == 4:
            print('Cerrando Sesión de Compras en CineHoy\n')
            estapa_menu = False

        else:
            print('Opción inválida, intente nuevamente o contacte al administrador.')
                

print (user)

# reserva_asiento(asientos_cine, 10)
# reserva_asiento(asientos_cine, 43)
# reserva_asiento(asientos_cine, 23)
# reserva_asiento(asientos_cine, 12)

resultado = np.array(render_asientos_usados(asientos_cine))
cine_matriz = resultado.reshape(5, 10)

pantalla = f'\t[*** PANTALLA CINE ***]\n {cine_matriz}'

# print(pantalla)