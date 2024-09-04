from models import bd


class Proveedor:
    def __init__(self):
        self.datos = bd.ControlDatos("proveedores.json")
        self.proveedores = self.datos.cargar_datos()

    def registrar_proveedor(self, nombre, direccion, telefono):
        if nombre not in self.proveedores:
            proveedor = {
                "direccion": direccion,
                "telefono": telefono,
                "productos": []
            }
            self.proveedores[nombre] = proveedor
            self.datos.actualizar_datos(self.proveedores)
            return True
        return False

    def agregar_producto(self, nombre_proveedor, producto):
        if nombre_proveedor in self.proveedores:
            if producto not in self.proveedores[nombre_proveedor]["productos"]:
                self.proveedores[nombre_proveedor]["productos"].append(
                    producto)
                self.datos.actualizar_datos(self.proveedores)
                return True
        return False

    def eliminar_producto(self, nombre_proveedor, producto):
        if nombre_proveedor in self.proveedores:
            if producto in self.proveedores[nombre_proveedor]["productos"]:
                self.proveedores[nombre_proveedor]["productos"].remove(
                    producto)
                self.datos.actualizar_datos(self.proveedores)
                return True
        return False

    def consultar_proveedor(self, nombre_proveedor):
        if nombre_proveedor in self.proveedores:
            return self.proveedores[nombre_proveedor]
        return None
