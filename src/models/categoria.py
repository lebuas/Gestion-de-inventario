from models import bd


class Categoria:
    def __init__(self):
        self.datos = bd.ControlDatos("categorias.json")
        self.categorias = self.datos.cargar_datos()

    def registrar_categoria(self, nombre, descripcion):
        if nombre not in self.categorias:
            categoria = {
                "descripcion": descripcion,
                "productos": []
            }
            self.categorias[nombre] = categoria
            self.datos.actualizar_datos(self.categorias)
            return True
        return False

    def agregar_producto(self, nombre_categoria, producto):
        if nombre_categoria in self.categorias:
            if producto not in self.categorias[nombre_categoria]["productos"]:
                self.categorias[nombre_categoria]["productos"].append(producto)
                self.datos.actualizar_datos(self.categorias)
                return True
        return False

    def eliminar_producto(self, nombre_categoria, producto):
        if nombre_categoria in self.categorias:
            if producto in self.categorias[nombre_categoria]["productos"]:
                self.categorias[nombre_categoria]["productos"].remove(producto)
                self.datos.actualizar_datos(self.categorias)
                return True
        return False

    def consultar_categoria(self, nombre_categoria):
        if nombre_categoria in self.categorias:
            return self.categorias[nombre_categoria]
        return None
