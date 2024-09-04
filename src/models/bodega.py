from models import bd


class Bodega:
    def __init__(self):
        self.datos = bd.ControlDatos("bodegas.json")
        self.bodegas = self.datos.cargar_datos()

    def registrar_bodega(self, nombre, ubicacion, capacidad):
        if nombre not in self.bodegas:
            bodega = {
                "ubicacion": ubicacion,
                "capacidad_maxima": capacidad,
                "productos_almacenados": []
            }
            self.bodegas[nombre] = bodega
            self.datos.actualizar_datos(self.bodegas)
            return True
        return False

    def agregar_producto(self, nombre_bodega, producto, cantidad):
        if nombre_bodega in self.bodegas:
            productos = self.bodegas[nombre_bodega]["productos_almacenados"]
            for item in productos:
                if item["nombre"] == producto:
                    item["cantidad"] += cantidad
                    self.datos.actualizar_datos(self.bodegas)
                    return True
            productos.append({
                "nombre": producto,
                "cantidad": cantidad
            })
            self.datos.actualizar_datos(self.bodegas)
            return True
        return False

    def retirar_producto(self, nombre_bodega, producto, cantidad):
        if nombre_bodega in self.bodegas:
            productos = self.bodegas[nombre_bodega]["productos_almacenados"]
            for item in productos:
                if item["nombre"] == producto:
                    if item["cantidad"] >= cantidad:
                        item["cantidad"] -= cantidad
                        if item["cantidad"] == 0:
                            productos.remove(item)
                        self.datos.actualizar_datos(self.bodegas)
                        return True
                    return False
        return False

    def disponibilidad(self, nombre_bodega):
        if nombre_bodega in self.bodegas:
            return self.bodegas[nombre_bodega]["productos_almacenados"]
        return None

    def consultar_bodega(self, nombre_bodega):
        if nombre_bodega in self.bodegas:
            return self.bodegas[nombre_bodega]
        return None
