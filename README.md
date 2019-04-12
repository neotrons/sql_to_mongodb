## Migrar SQL a MongoDB

#### Requerimientos
* [Descargar e instalar python](https://www.python.org/downloads/release/python-368/) 3.5 o superior 
* instalar requerimientos del proyecto

```
pip install -r requirements.txt
```
    
#### Configuración
* Configurar la conexion SQL origen

```
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
```
* Configurar la conexion MongoDB destino

```
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
```

#### Mapeo de variables
Es la relacion entre los campos origen del SQL y los destinos en MondoDB. Se debe especificar el tipo de dato que se 
desea aplicar los tipos de datos aceptados son int, str, json sin embargo es posible crear extender estos tipos.
```
MAP = {
        "campo_origen_sql": {
            "type": "tipo", 
            "dest": "campo_destino_mongo"
        }
    }
```

#### Funciones de tipo peronalizados
Permite extender los tipos de datos o personalizar la conversion pormedio de funciones de python
```
def to_int_or_cero(v):
    return int(v, 0)
    
TIPO_FUNCIONES = {
    "int_or_cero": to_int_or_cero
}
```

#### Ejecutar.
El bloque que ejecuta la migración es 
```
if __name__ == "__main__":
    data_parser = sql(ORIGEN, MAP, TIPO_FUNCIONES)
    mongo(DESTINO, data_parser)
```

por lo tanto para ejecutar la migración solo hace falta ejecutar el archivo ejemplo:
```
python ejemplo.py
```