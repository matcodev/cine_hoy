def digito_verificador(rut):
    rut_invertido = str(rut)[::-1]
    valores = [2, 3, 4, 5, 6, 7]
    total = sum([int(rut_invertido[i]) * valores[i % 6]
                for i in range(len(rut_invertido))])
    resultado = 11-(total % 11)

    if resultado == 11:
        digito = 0
    elif resultado == 10:
        digito = "k"
    else:
        digito = resultado
    
    return digito

def valida_rut(rutUser):
    rut_sin_dv = rutUser.split("-")[0]
    rut_dv = rutUser.split("-")[1]
    isDV = str(digito_verificador(rut_sin_dv))

    if isDV == rut_dv.lower():
        return 1
    else:
        return 0

def valida_mayor_edad(edad):
    if edad >= 18:
        return 1
    else:
        return 0
