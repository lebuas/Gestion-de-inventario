from src.models import categoria


class InputCategorias:
    def __init__(self):
        self.instancia = categoria.Categoria()

    def registrar_categoria(self):
        try:
            nombre = input("Ingrese el nombre de la categoría: ")
            descripcion = input("Ingrese la descripción de la categoría: ")

            if self.instancia.registrar_categoria(nombre, descripcion):
                print("Categoría registrada con éxito.")
            else:
                print("La categoría ya está registrada.")
        except Exception as e:
            print(f"Ha ocurrido un error al registrar la categoría: {e}.")

    def agregar_producto_categoria(self):
        try:
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            producto = input("Ingrese el nombre del producto a agregar: ")

            if self.instancia.agregar_producto(nombre_categoria, producto):
                print("Producto agregado a la categoría con éxito.")
            else:
                print("La categoría no existe o el producto ya está en la categoría.")
        except Exception as e:
            print(
                f"Ha ocurrido un error al agregar el producto a la categoría: {e}.")

    def eliminar_producto_categoria(self):
        try:
            nombre_categoria = input("Ingrese el nombre de la categoría: ")
            producto = input("Ingrese el nombre del producto a eliminar: ")

            if self.instancia.eliminar_producto(nombre_categoria, producto):
                print("Producto eliminado de la categoría con éxito.")
            else:
                print("La categoría no existe o el producto no está en la categoría.")
        except Exception as e:
            print(
                f"Ha ocurrido un error al eliminar el producto de la categoría: {e}.")

    def consultar_categoria(self):
        try:
            nombre_categoria = input(
                "Ingrese el nombre de la categoría a consultar: ")
            categoria_info = self.instancia.consultar_categoria(
                nombre_categoria)

            if categoria_info:
                print("\nInformación de la Categoría:")
                print(f"Nombre: {nombre_categoria}")
                print(f"Descripción: {categoria_info['descripcion']}")
                print("Productos:")
                if categoria_info["productos"]:
                    for producto in categoria_info["productos"]:
                        print(f" - {producto}")
                else:
                    print("No hay productos en esta categoría.")
            else:
                print("La categoría no se encuentra registrada.")
        except Exception as e:
            print(f"Ha ocurrido un error al consultar la categoría: {e}.")
