import json


class Consultas:
    def __init__(self, registros):
        self.registros = registros

    def consultar_informacion_productos(self, nombre_producto):
        producto = self.registros.productos.get(nombre_producto)
        if producto:
            return producto
        return f"Producto '{nombre_producto}' no encontrado."

    def consultar_informacion_categorias(self, nombre_categoria):
        categoria = self.registros.categorias.get(nombre_categoria)
        if categoria:
            return categoria
        return f"Categoría '{nombre_categoria}' no encontrada."

    def consultar_informacion_proveedores(self, nombre_proveedor):
        proveedor = self.registros.proveedores.get(nombre_proveedor)
        if proveedor:
            return proveedor
        return f"Proveedor '{nombre_proveedor}' no encontrado."

    def consultar_informacion_bodegas(self, nombre_bodega):
        bodega = self.registros.bodegas.get(nombre_bodega)
        if bodega:
            return bodega
        return f"Bodega '{nombre_bodega}' no encontrada."

    def generar_informes_stock(self):
        informes = []
        for nombre_bodega, bodega in self.registros.bodegas.items():
            informe = {
                'bodega': nombre_bodega,
                'productos': bodega.get('productos_almacenados', [])
            }
            informes.append(informe)
        return informes
