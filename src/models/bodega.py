from models import dataBase


class Bodega:
    def __init__(self):
        self.bodega = {}

    def registrar_bodega(self, nombre, ubicacion, capacidad, producto, cantidad):
        bodega = {
            "nombre_bodega": nombre,
            "ubicacion": ubicacion,
            "capacidad_maxima": capacidad,
            "productos_almacenado": [{
                "nombre": producto[0],
                "cantidad": cantidad
            }]
        }

        return bodega

    def agregar_productos(self):
        pass

    def retirar_productos(self):
        pass

    def disponibilidad(self):
        pass

    def consultar_bodegas(self):
        pass
