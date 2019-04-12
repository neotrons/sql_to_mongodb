import pyodbc
import json
from pymongo import MongoClient


def to_int(v):
    return int(v) if v is not None else v


def to_str(v):
    return str(v).strip() if v is not None else v


def to_json(v):
    return json.loads(v) if v is not None else v


TIPOS = {
    "int": to_int,
    "str": to_str,
    "json": to_json
}


def to_dict(cursor, mapper, functions):
    for f in functions:
        TIPOS[f] = functions[f]

    desc = [col[0] for col in cursor.description]
    datos = cursor.fetchall()
    stage_dict = [dict(zip(desc, dato)) for dato in datos]
    result_dict = []
    for dato in stage_dict:
        newdato = {}
        for k, v in dato.items():
            if k in mapper:
                if mapper[k]['type'] in TIPOS:
                    d = TIPOS[mapper[k]['type']](v)
                else:
                    d = v
                newdato[mapper[k]["dest"]] = d
        if newdato:
            result_dict.append(newdato)
    return result_dict


def mongo(ops, datos):
    config = ops['config']
    client = MongoClient(config['host'], config['port'])
    db = client[config["name"]]
    data = db[ops["collection"]].insert(datos)
    print("Se inserto correctamente {} documentos".format(len(data)))
    return data


def sql(ops, mapper, functions):
    config = ops['config']
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s'
                          % (config["host"], config["name"], config["user"], config["password"]))
    cursor = cnxn.cursor()
    query = "SELECT * FROM {}".format(ops['table'])
    cursor.execute(query)
    cabeceras = [col[0] for col in cursor.description]
    datos = to_dict(cursor, mapper, functions)
    return datos
