

class RelacionesEntidades:
    def __init__(self, datos):
        self.productos = {p['nombre']: p for p in datos.get('productos', [])}
        self.categorias = {c['nombre']: c for c in datos.get('categorias', [])}
        self.proveedores = {
            p['nombre']: p for p in datos.get('proveedores', [])
        }
        self.bodegas = {b['nombre']: b for b in datos.get('bodegas', [])}

    def eliminar_producto_de_categoria(self, producto, categoria):
        if producto in self.productos:
            if self.productos[producto].get('categoria_id') == categoria:
                self.productos[producto]['categoria_id'] = None
            else:
                print("El producto no está asignado a esta categoría.")
        else:
            print("Producto no encontrado.")

    def agregar_producto_a_proveedor(self, producto, proveedor):
        if producto in self.productos and proveedor in self.proveedores:
            if producto not in self.proveedores[proveedor][
                    'productos_suministrados'
            ]:
                self.proveedores[proveedor]['productos_suministrados'].append(
                    producto)
        else:
            print("Producto o proveedor no encontrados.")

    def eliminar_producto_de_proveedor(self, producto, proveedor):
        if proveedor in self.proveedores:
            if producto in self.proveedores[proveedor][
                'productos_suministrados'
            ]:
                self.proveedores[proveedor]['productos_suministrados'].remove(
                    producto)
            else:
                print(
                    "El producto no está en la lista de suministros del proveedor.")
        else:
            print("Proveedor no encontrado.")

    def agregar_producto_a_bodega(self, producto, bodega, cantidad):
        if producto in self.productos and bodega in self.bodegas:
            bodega_info = self.bodegas[bodega]
            productos = bodega_info['productos_almacenados']
            for p in productos:
                if p['nombre'] == producto:
                    p['cantidad'] += cantidad
                    break
            else:
                productos.append({'nombre': producto, 'cantidad': cantidad})
        else:
            print("Producto o bodega no encontrados.")

    def retirar_producto_de_bodega(self, producto, bodega, cantidad):
        if bodega in self.bodegas:
            bodega_info = self.bodegas[bodega]
            productos = bodega_info['productos_almacenados']
            for p in productos:
                if p['nombre'] == producto:
                    if p['cantidad'] >= cantidad:
                        p['cantidad'] -= cantidad
                        if p['cantidad'] == 0:
                            productos.remove(p)
                    else:
                        print("No hay suficiente cantidad para retirar.")
                    break
            else:
                print("Producto no encontrado en la bodega.")
        else:
            print("Bodega no encontrada.")

    def consultar_disponibilidad_en_bodega(self, producto, bodega):
        if bodega in self.bodegas:
            bodega_info = self.bodegas[bodega]
            productos = bodega_info['productos_almacenados']
            for p in productos:
                if p['nombre'] == producto:
                    return p['cantidad']
            return 0
        else:
            print("Bodega no encontrada.")
            return None
