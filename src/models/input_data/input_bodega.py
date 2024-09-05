from src.models import bodega


class InputBodega:

    def __init__(self):
        self.instancia = bodega.Bodega()

    def registrar_bodega(self):
        try:
            nombre = input("Ingrese el nombre de la bodega: ")
            ubicacion = input("Ingrese la ubicación de la bodega: ")
            capacidad = int(
                input("Ingrese la capacidad máxima de la bodega: ")
            )

            if self.instancia.registrar_bodega(nombre, ubicacion, capacidad):
                print("Bodega registrada con éxito.")
            else:
                print("La bodega ya está registrada.")
        except Exception as e:
            print(f"Ha ocurrido un error al registrar la bodega: {e}.")

    def agregar_producto_bodega(self):
        try:
            nombre_bodega = input("Ingrese el nombre de la bodega: ")
            producto = input("Ingrese el nombre del producto a agregar: ")
            cantidad = int(
                input("Ingrese la cantidad del producto a agregar: ")
            )

            if self.instancia.agregar_producto(
                nombre_bodega, producto, cantidad
            ):
                print("Producto agregado a la bodega con éxito.")
            else:
                print(
                    """La bodega no existe o ha ocurrido un error
                    al agregar el producto."""
                )
        except Exception as e:
            print(
                f"Ocurrido un error al agregar el producto a la bodega: {e}."
            )

    def retirar_producto_bodega(self):
        try:
            nombre_bodega = input("Ingrese el nombre de la bodega: ")
            producto = input("Ingrese el nombre del producto a retirar: ")
            cantidad = int(
                input("Ingrese la cantidad del producto a retirar: ")
            )

            if self.instancia.retirar_producto(
                nombre_bodega, producto, cantidad
            ):
                print("Producto retirado de la bodega con éxito.")
            else:
                print(
                    "La bodega no existe o el producto no está en la bodega, "
                    "o la cantidad a retirar es mayor a la disponible."
                )
        except Exception as e:
            print(
                f"Ocurrido un error al retirar el producto de la bodega: {e}."
            )

    def consultar_disponibilidad_bodega(self):
        try:
            nombre_bodega = input(
                "Ingrese el nombre de la bodega a consultar: "
            )
            productos = self.instancia.disponibilidad(nombre_bodega)

            if productos is not None:
                print("\nDisponibilidad de Productos en la Bodega:")
                if productos:
                    for item in productos:
                        print(
                            f"Producto: {item['nombre']}, "
                            f"Cantidad: {item['cantidad']}"
                        )
                else:
                    print("No hay productos almacenados en esta bodega.")
            else:
                print("La bodega no se encuentra registrada.")
        except Exception as e:
            print(
                f"""Ocurrio un error al consultar
                la disponibilidad de la bodega: {e}."""
            )
