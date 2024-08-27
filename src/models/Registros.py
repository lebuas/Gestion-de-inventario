
class Registros:

    def __init__(self, datos):
        self.indice = datos

    def registrar_productos(self, nombre, descripcion, precio, stock, categoria):
        if self.existencia(nombre):
            self.indice[nombre] = {
                'nombre': nombre,
                'descripcion': descripcion,
                'precio': precio,
                'stock': stock,
                'categoria_id': categoria
            }

    def registrar_categorias(self, nombre, descripcion):
        if self.existencia(nombre):
            self.indice[nombre] = {
                'nombre': nombre,
                'descripcion': descripcion
            }

    def registrar_proveedores(self, nombre, direccion, telefono, productos):
        if self.existencia(nombre):
            self.indice[nombre] = {
                'nombre': nombre,
                'direccion': direccion,
                'telefono': telefono,
                'productos_suministrados': productos
            }

    def registrar_bodegas(self, nombre, ubicacion, capacidad, productos):
        if self.existencia(nombre):
            self.indice[nombre] = {
                'nombre': nombre,
                'ubicacion': ubicacion,
                'capacidad_maxima': capacidad,
                'productos_almacenados': productos
            }

    def existencia(self, name):
        if name in self.indice:
            print(f"El nombre '{name}' ya se encuentra en los datos.")
            return False
        return True
