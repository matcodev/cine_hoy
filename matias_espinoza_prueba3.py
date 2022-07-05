from datetime import date
from funciones_prueba3 import valida_rut
from funciones_prueba3 import valida_mayor_edad

rut_afiliados = []
nombre_afiliados = []
apellido_paternos_afiliados = []
edad_afiliados = []
estado_civil_afiliados = []
genero_afiliados = []
fecha_afiliacion_afiliados = []

afiliado = []

estados_civiles = {
    'c' : 'Casado',
    's' : 'Soltero',
    'v' : 'Viudo'
}

generos = {
    'm' : 'Masculino',
    'f' : 'Femenino'
}

etapa_menu = False

while etapa_menu == False:
    try:
        respuesta_menu = int(input(f'*** Bienvenido a Isapre Vida Salud ***\n 1.- Grabar Afiliado\n 2.- Buscar Afiliado\n 3.- Imprimir Certificados\n 4.- Salir\n'))
    except:
        print('Ups! Opción inválida, vuelva a intentarlo.')
    else:
        if respuesta_menu == 1:
            add_rut = False

            while add_rut == False:
                try:
                    rut_user = input('A continuación, ingrese su rut sin puntos y con guión para grabar (ejemplo: 12345678-9) ->\n')
                    
                    rut_validado = valida_rut(rut_user)
                    
                    if rut_validado == 1:
                        afiliado.append(rut_user)
                        add_rut = True
                    else:
                        print('RUT ingresado no es válido. Revise nuevamente el digito verificador!')
                except:
                    print('RUT inválido, revise o vuelva a intentarlo!\n')
            
            add_nombre = False

            while add_nombre == False:
                try:
                    respuesta_nombre_afiliado = input('Ingrese su nombre ->\n')
                    afiliado.append(respuesta_nombre_afiliado)

                    respuesta_apellido_afiliado = input('Ingrese su apellido Paterno ->\n')
                    afiliado.append(respuesta_apellido_afiliado)
                    
                    add_nombre = True
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')
                    
            add_edad = False

            while add_edad == False:
                try:
                    respuesta_edad_afiliado = int(input('Ingrese su edad ->\n'))
                    edad_validada = valida_mayor_edad(respuesta_edad_afiliado)

                    if edad_validada == 1:
                        afiliado.append(respuesta_edad_afiliado)
                        add_edad = True
                    else:
                        print('Edad no válida para ser registrado como afiliado. Consulte con un administrador o intente más tarde.')
                except:
                    print('Verifique que los datos estén correctos o vuelva a intentarlo!')

            add_estado_civil = False

            while add_estado_civil == False:
                try:
                    respuesta_estado_civil = input('Indique su Estado Civil según la letra que corresponda en el menú:\n C = Casada \n S = Soltero \n V = Viudo')
                    resp_estado_civil = respuesta_estado_civil.lower()
                 
                    if resp_estado_civil == 'c' or resp_estado_civil == 's' or resp_estado_civil == 'v':
                        for i in estados_civiles:
                            if i == resp_estado_civil:
                                afiliado.append(estados_civiles[i])
                    
                        add_estado_civil = True
                    else:
                        print('Opción no disponible. Debes aceptar solo opciones válidas.')

                except:
                    print("Error en agregar Estado Civil. Debes aceptar solo opciones válidas.")
            
            add_genero = False

            while add_genero == False:
                try:
                    respuesta_genero = input('Ingrese la opción que represente su genero: \n M = Masculino \n F = Femenino \n')
                    resp_genero = respuesta_genero.lower()

                    if resp_genero == 'f' or resp_genero == 'm':
                        for i in generos:
                            if i == resp_genero:
                                afiliado.append(generos[i])
                        
                        add_genero = True
                    else:
                        print('Opción no disponible. debes aceptar solo opciones válidas.')
                
                except:
                    print('Error al ingresar su genero. Intente nuevamente.')
           
            add_confirma_fecha = False

            while add_confirma_fecha == False: 
                try:
                    fecha_registro = date.today()
                    fecha_formated = fecha_registro.strftime("%d/%m/%Y")
                    respuesta_fecha = int(input(f'Desea confirmar que la fecha para afiliarse es {fecha_formated}:\n 1 = Si \n 2 = No'))

                    if respuesta_fecha == 1:
                        afiliado.append(fecha_formated)
                except:
                   print('Error al ingresar su genero. Intente nuevamente.')
        elif respuesta_menu == 4:
            print('Cerrando Sesión...')
            etapa_menu = True

        else:
            print('Opción inválida, intente nuevamente o contacte al administrador.')

print(afiliado)