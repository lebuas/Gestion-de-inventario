from models import bd


class Producto:

    def __init__(self):
        # (name archivo json con los datos, clave de la estructura json)
        self.datos = bd.ControlDatos("productos.json", "productos")
        self.productos = self.datos.cargar_datos()

    def registrar_productos(self, name, descripcion, precio, stock, categoria):
        if name not in self.productos["productos"]:
            producto = {
                "descripcion": descripcion,
                "precio": precio,
                "stock": stock,
                "categoria": categoria
            }
            self.productos["productos"][name] = producto
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def agrega_stock(self, producto, nuevo_stock):
        if producto in self.productos["productos"]:
            self.productos["productos"][producto]["stock"] += nuevo_stock
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def retirar_stock(self, producto, stock_a_retirar):
        productos_actuales = self.productos["productos"]
        if producto in productos_actuales and productos_actuales[
                producto]["stock"] >= stock_a_retirar:

            self.productos["productos"][producto]["stock"] -= stock_a_retirar
            self.datos.actualizar_datos(self.productos)
            return True
        return False

    def calcular_total_stock(self):
        total_stock = 0.0

        for producto in self.productos["productos"].values():
            precio = producto["precio"]
            stock = producto["stock"]
            total_stock += precio * stock
        return total_stock

    def consulta_producto(self, producto):
        lista_productos = self.productos["productos"]
        if producto in lista_productos:
            return lista_productos[producto]
        return None
