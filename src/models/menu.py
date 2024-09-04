
class Menu:
    def __init__(self):
        self.run()

    def run(self):
        while True:
            print("\nSistema de Gestión de Inventario")
            print("1. Opciones de Producto")
            print("2. Opciones de Categoría")
            print("3. Opciones de Proveedor")
            print("4. Opciones de Bodega")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.menu_producto()
            elif opcion == '2':
                self.menu_categoria()
            elif opcion == '3':
                self.menu_proveedor()
            elif opcion == '4':
                self.menu_bodega()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_producto(self):
        while True:
            print("\nOpciones de Producto")
            print("1. Registrar Producto")
            print("2. Agregar Stock a Producto")
            print("3. Retirar Stock de Producto")
            print("4. Calcular Valor Total del Stock")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_producto()
            elif opcion == '2':
                self.agregar_stock_producto()
            elif opcion == '3':
                self.retirar_stock_producto()
            elif opcion == '4':
                self.calcular_valor_total_stock()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_categoria(self):
        while True:
            print("\nOpciones de Categoría")
            print("1. Registrar Categoría")
            print("2. Agregar Producto a Categoría")
            print("3. Eliminar Producto de Categoría")
            print("4. Consultar Información de Categoría")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_categoria()
            elif opcion == '2':
                self.agregar_producto_categoria()
            elif opcion == '3':
                self.eliminar_producto_categoria()
            elif opcion == '4':
                self.consultar_categoria()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_proveedor(self):
        while True:
            print("\nOpciones de Proveedor")
            print("1. Registrar Proveedor")
            print("2. Agregar Producto a Proveedor")
            print("3. Eliminar Producto de Proveedor")
            print("4. Consultar Información de Proveedor")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_proveedor()
            elif opcion == '2':
                self.agregar_producto_proveedor()
            elif opcion == '3':
                self.eliminar_producto_proveedor()
            elif opcion == '4':
                self.consultar_proveedor()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def menu_bodega(self):
        while True:
            print("\nOpciones de Bodega")
            print("1. Registrar Bodega")
            print("2. Agregar Producto a Bodega")
            print("3. Retirar Producto de Bodega")
            print("4. Consultar Disponibilidad de Producto en Bodega")
            print("5. Volver al Menú Principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.registrar_bodega()
            elif opcion == '2':
                self.agregar_producto_bodega()
            elif opcion == '3':
                self.retirar_producto_bodega()
            elif opcion == '4':
                self.consultar_disponibilidad_bodega()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")
