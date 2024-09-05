from src.models.input_data import input_producto
from src.models.input_data import input_bodega
from src.models.input_data import input_categoria
from src.models.input_data import input_proveedor


class Menu:
    def __init__(self):
        self.menu_options = {
            '1': ("Opciones de Producto", self.menu_producto),
            '2': ("Opciones de Categoría", self.menu_categoria),
            '3': ("Opciones de Proveedor", self.menu_proveedor),
            '4': ("Opciones de Bodega", self.menu_bodega),
            '0': ("Salir", None)
        }
        self.run()

    def run(self):
        while True:
            print("\nSistema de Gestión de Inventario")
            for key, (description, _) in self.menu_options.items():
                print(f"{key}. {description}")

            opcion = input("Seleccione una opción: ")

            if opcion in self.menu_options:
                _, action = self.menu_options[opcion]
                if action:
                    action()
                else:
                    break
            else:
                print("Opción no válida. Intente de nuevo.")

    def submenu(self, title, options):
        while True:
            print(f"\n{title}")
            for key, (description, _) in options.items():
                print(f"{key}. {description}")

            opcion = input("Seleccione una opción: ")

            if opcion in options:
                _, action = options[opcion]
                if action:
                    action()
                else:
                    break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_producto(self):
        menu = input_producto.IputProdcutos()
        options = {
            '1': ("Registrar Producto", menu.registrar_producto),
            '2': ("Agregar Stock a Producto", menu.agregar_stock_producto),
            '3': ("Retirar Stock de Producto", menu.retirar_stock_producto),
            '4': ("Calcular Valor Total del Stock",
                  menu.calcular_valor_total_stock),
            '5': ("Consultar producto", menu.consultar_productos),
            '0': ("Volver al Menú Principal", None)
        }
        self.submenu("Opciones de Producto", options)

    def menu_categoria(self):
        menu = input_categoria.InputCategorias()
        options = {
            '1': ("Registrar Categoría", menu.registrar_categoria),
            '2': ("Agregar Producto a Categoría",
                  menu.agregar_producto_categoria),
            '3': ("Eliminar Producto de Categoría",
                  menu.eliminar_producto_categoria),
            '4': ("Consultar Información de Categoría",
                  menu.consultar_categoria),
            '0': ("Volver al Menú Principal", None)
        }
        self.submenu("Opciones de Categoría", options)

    def menu_proveedor(self):
        menu = input_proveedor.InputPorveedores()
        options = {
            '1': ("Registrar Proveedor", menu.registrar_proveedor),
            '2': ("Agregar Producto a Proveedor",
                  menu.agregar_producto_proveedor),
            '3': ("Eliminar Producto de Proveedor",
                  menu.eliminar_producto_proveedor),
            '4': ("Consultar Información de Proveedor",
                  menu.consultar_proveedor),
            '0': ("Volver al Menú Principal", None)
        }
        self.submenu("Opciones de Proveedor", options)

    def menu_bodega(self):
        menu = input_bodega.InputBodega()
        options = {
            '1': ("Registrar Bodega", menu.registrar_bodega),
            '2': ("Agregar Producto a Bodega", menu.agregar_producto_bodega),
            '3': ("Retirar Producto de Bodega", menu.retirar_producto_bodega),
            '4': ("Consultar Disponibilidad de Producto en Bodega",
                  menu.consultar_disponibilidad_bodega),
            '0': ("Volver al Menú Principal", None)
        }
        self.submenu("Opciones de Bodega", options)
