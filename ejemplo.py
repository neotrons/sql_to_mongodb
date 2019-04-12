from utils.sql_to_mongo import sql, mongo

ORIGEN = {
    "type": 'sql',
    "config": {
        "host": 'localhost',
        "name": 'BD_SQL_ORIGEN',
        "user": 'usuario',
        "password": 'xxxxxxx'
    },

    "table": '[ESQUEMA].[TABLA]',  # Esquema es opcional
}

DESTINO = {
    "type": 'mongo',
    "config": {
        "host": 'localhost',
        "name": 'BD_MONGO',
        "user": 'usuario',
        "password": 'xxxxxxxx',
        "port": 27017
    },

    "collection": 'nombre_coleccion'
}

"""Mapear origen y destino
{
    "campo_origen_sql": {
        "type": "tipo", 
        "dest": "campo_destino_mongo"
    }
}

type: int, str, json

"""
MAP = {
    "cod_cuadro": {
        "type": "int",
        "dest": "cod_cuadro"
    },

    "tomo": {
        "type": "str",
        "dest": "tomo"
    },

    "titulo_cuadro": {
        "type": "str",
        "dest": "titulo_cuadro"
    },

    "nombre_cuadro": {
        "type": "str",
        "dest": "nombre_cuadro"
    },

    "pie_pagina": {
        "type": "str",
        "dest": "pie_pagina"
    },

    "filas": {
        "type": "json",
        "dest": "filas"
    }
}

""" Agrega nuevos tipos

def to_int_or_cero(v):
    return int(v, 0)
    
TIPO_FUNCIONES = {
    "int_or_cero": to_int_or_cero
}

int_or_cero esta disponible como nuevo type
"""
TIPO_FUNCIONES = {}

if __name__ == "__main__":
    data_parser = sql(ORIGEN, MAP, TIPO_FUNCIONES)
    mongo(DESTINO, data_parser)
