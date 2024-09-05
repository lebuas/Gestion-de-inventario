from src.models import bd


class Producto:
    def __init__(self):
        self.datos = bd.ControlDatos("productos.json")
        self.productos = self.datos.cargar_datos()

    def registrar_producto(self, nombre, descripcion, precio, stock,
                           categoria):
        if nombre not in self.productos:
            producto = {
                "descripcion": descripcion,
                "precio": precio,
                "stock": stock,
                "categoria": categoria
            }
            self.productos[nombre] = producto
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def agregar_stock(self, nombre, nuevo_stock):
        if nombre in self.productos:
            self.productos[nombre]["stock"] += nuevo_stock
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def retirar_stock(self, nombre, stock_a_retirar):
        if nombre in self.productos and self.productos[nombre][
                "stock"] >= stock_a_retirar:

            self.productos[nombre]["stock"] -= stock_a_retirar
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def calcular_total_stock(self):
        total_stock = 0.0
        for producto in self.productos.values():
            precio = producto["precio"]
            stock = producto["stock"]
            total_stock += precio * stock
        return total_stock

    def consulta_producto(self, nombre):
        if nombre in self.productos:
            return self.productos[nombre]
        return None
