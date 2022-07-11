user_t = {}

user_t["datos_personales"] = {}
user_t["datos_personales"]["rut"] = '18355317-8'
user_t["datos_personales"]["nombre"] = 'Matias'
user_t["datos_personales"]["apellido"] = 'Espinoza'

user_t["fase_compra"] = {}
user_t["fase_compra"]["tipo_producto"] = 'Ticket VIP'
user_t["fase_compra"]["cantidad_producto"] = 2


# print(user_t)
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
