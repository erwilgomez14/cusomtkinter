import pymongo

def conectar():
    cliente = pymongo.MongoClient('mongodb+srv://spynter:FT6L38hPfWlovirA@cluster0.la6e0.mongodb.net/?retryWrites=true&w=majority')
    db = cliente["mi_base_de_datos_maki_sushi"]
    return db

def guardar_usuario(nombre, correo, contraseña):
    db = conectar()
    coleccion = db["usuarios"]
    nuevo_usuario = {"nombre": nombre, "correo": correo, "contraseña": contraseña}
    coleccion.insert_one(nuevo_usuario)

