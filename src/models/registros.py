
class Registros:

    def registrar_productos(self, nombre, descripcion, precio, stock, categoria):
        producto = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }
        return producto

    def registrar_categorias(self, nombre, descripcion):
        categoria = {
            "nombre": nombre,
            "descripcion": descripcion
        }
        return categoria

    def registrar_proveedores(self, nombre, direccion, telefono, productos):
        proveedor = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "productos": productos
        }
        return proveedor

    def registrar_bodegas(self, nombre, ubicacion, capacidad, producto: list):
        bodega = {
            "nombre_bodega": nombre,
            "ubicacion": ubicacion,
            "capacidad_maxima": capacidad,
            "productos_almacenado": [{
                "nombre": producto[0],
                "cantidad": producto[1]
            }]
        }

        return bodega
