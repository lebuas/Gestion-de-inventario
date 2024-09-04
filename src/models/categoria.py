class Categoria:
    def __init__(self):
        self.categoria = {}

    def regitrar_categoria(self, nombre, descripcion):
        categoria = {
            "nombre": nombre,
            "descripcion": descripcion
        }
        return categoria

    def agregar_producto(self):
        pass

    def eliminar_producto(self):
        pass

    def consultar_categoria(self):
        pass
