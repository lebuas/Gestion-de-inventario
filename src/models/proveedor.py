class Proveedor:
    def __init__(self):
        self.proveedores

    def registrar_proveedores(self, nombre, direccion, telefono, productos):
        proveedor = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "productos": productos
        }
        return proveedor

    def egragar_producto(self):
        pass

    def eliminar_producto(self):
        pass

    def consultar_producto(self):
        pass
