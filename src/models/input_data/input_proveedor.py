from src.models import proveedor


class InputPorveedores:
    def __init__(self):
        self.instancia = proveedor.Proveedor()

    def registrar_proveedor(self):

        try:
            nombre = input("Ingrese el nombre del proveedor: ")
            direccion = input("Ingrese la dirección del proveedor: ")
            telefono = input("Ingrese el teléfono del proveedor: ")

            if self.instancia.registrar_proveedor(nombre, direccion, telefono):
                print("Proveedor registrado con éxito.")
            else:
                print("El proveedor ya está registrado.")
        except Exception as e:
            print(f"Ha ocurrido un error al registrar el proveedor: {e}.")

    def agregar_producto_proveedor(self):
        try:
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")
            producto = input("Ingrese el nombre del producto a agregar: ")

            if self.instancia.agregar_producto(nombre_proveedor, producto):
                print("Producto agregado al proveedor con éxito.")
            else:
                print(
                    "El proveedor no existe o",
                    "el producto ya está en la lista del proveedor."
                )
        except Exception as e:
            print(
                f"Error al agregar el producto al proveedor: {e}.")

    def eliminar_producto_proveedor(self):
        try:
            nombre_proveedor = input("Ingrese el nombre del proveedor: ")
            producto = input("Ingrese el nombre del producto a eliminar: ")

            if self.instancia.eliminar_producto(nombre_proveedor, producto):
                print("Producto eliminado del proveedor con éxito.")
            else:
                print("El proveedor no existe o",
                      "el producto no está en la lista del proveedor."
                      )

        except Exception as e:
            print(
                f"Error al eliminar el producto del proveedor: {e}.")

    def consultar_proveedor(self):

        try:
            nombre_proveedor = input(
                "Ingrese el nombre del proveedor a consultar: ")
            proveedor_info = self.instancia.consultar_proveedor(
                nombre_proveedor)

            if proveedor_info:
                print("\nInformación del Proveedor:")
                print(f"Nombre: {nombre_proveedor}")
                print(f"Dirección: {proveedor_info['direccion']}")
                print(f"Teléfono: {proveedor_info['telefono']}")
                print("Productos:")
                if proveedor_info["productos"]:
                    for producto in proveedor_info["productos"]:
                        print(f" - {producto}")
                else:
                    print("No hay productos registrados para este proveedor.")
            else:
                print("El proveedor no se encuentra registrado.")
        except Exception as e:
            print(f"Ha ocurrido un error al consultar el proveedor: {e}.")
            pass
