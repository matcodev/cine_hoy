import numpy as np

def reserva_asiento(asientos, reserva):
    asientos[np.absolute(asientos) == reserva] = -1
    return asientos

def render_asientos_usados(reservados):
    usados_asientos = []
    for asientos in reservados:
        if asientos == -1:
            usados_asientos.append('X')
        else:
            usados_asientos.append(asientos)
    
    return usados_asientos

def digito_verificador(rut):
    rut_invertido = str(rut)[::-1]
    valores = [2, 3, 4, 5, 6, 7]
    total = sum([int(rut_invertido[i]) * valores[i % 6] for i in range(len(rut_invertido))])
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
        return True
    else:
        return False

def getNameDict(dict, respuesta):
    for nameItem, rsp in dict.items():
        if rsp["respuesta"] == respuesta:
            return rsp["nombre"]

def getEstadoDict(dict, respuesta):
    for nameItem, rsp in dict.items():
        if rsp["respuesta"] == respuesta:
            return rsp["estado"]

def getValorDict(dict, respuesta):
    for nameItem, rsp in dict.items():
        if rsp["respuesta"] == respuesta:
            return rsp["valor"]

def getHorarioFuncion(dict, respuesta):
    for nameItem, rsp in dict.items():
        if respuesta == int(nameItem):
            for hora in rsp["horarios"]:
                return hora

# def getValores(tipoTicket, qTicket, tipoPalomitas, qPalomitas, tipoBebida, qBebidas):
#     for rspTicket in tickets_entradas:
#            if tickets_entradas[rspTicket]["respuesta"] == tipoTicket:
#                subTotalTicket = tickets_entradas[rspTicket]["valor"] * qTicket
               
#                for rspPalomitas in palomitas:
#                     if palomitas[rspPalomitas]["respuesta"] == tipoPalomitas:
#                         subTotalPalomitas = palomitas[rspPalomitas]["valor"] * qPalomitas

#                         for rspBebida in bebidas:
#                             if bebidas[rspBebida]["respuesta"] == tipoBebida:
#                                 subTotalBebida = bebidas[rspBebida]["valor"] * qBebidas

#     return subTotalTicket + subTotalPalomitas + subTotalBebida