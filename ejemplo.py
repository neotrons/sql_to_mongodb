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
    "campo_origen_sql": {
        "type": "tipo",
        "dest": "campo_destino_mongo"
    },

    "nombre": {
        "type": "str",
        "dest": "nombre"
    },

    "apellidopat": {
        "type": "str",
        "dest": "apellido_paterno"
    },

    "edad": {
        "type": "int",
        "dest": "edad"
    }
}

""" Agrega nuevos tipos

def to_int_or_cero(v, **kwargs):
    return int(v or 0)
    
TIPO_FUNCIONES = {
    "int_or_cero": to_int_or_cero
}

int_or_cero esta disponible como nuevo type para aplicar en map

MAP = {
    ....
    "edad": {
        "type": "int_or_cero",
        "dest": "edad"
    }
}    
"""
TIPO_FUNCIONES = {}

if __name__ == "__main__":
    data_parser = sql(ORIGEN, MAP, TIPO_FUNCIONES)
    mongo(DESTINO, data_parser)
