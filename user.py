users_bd = {}

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
            'numero_asiento': None,
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
            'valor_total' : int(2500)
        }
    }
}