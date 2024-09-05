from src.models import producto


class IputProdcutos:
    def __init__(self):
        self.instancia = producto.Producto()
        pass

    def registrar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = float(input("Ingrese el stock inicial del producto: "))
            categoria = input("Ingrese una categoría para el producto: ")

            if self.instancia.registrar_producto(nombre, descripcion, precio,
                                                 stock, categoria):
                print("Producto creado con éxito.")
            else:
                print("El producto ya se encuentra registrado.")

        except ValueError as ve:
            print(f"Error de valor: {ve}. Por favor, ingrese un valor válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}.")

    def agregar_stock_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = float(input("Ingrese la cantidad de stock a agregar: "))

            if self.instancia.agregar_stock(nombre, cantidad):
                print("Stock agregado exitosamente.")
            else:
                print("El producto no se encuentra registrado.")
        except ValueError as ve:
            print(f"Error de valor: {ve}. Por favor, ingrese un valor válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}.")

    def retirar_stock_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = float(input("Ingrese la cantidad de stock a retirar: "))

            if self.instancia.retirar_stock(nombre, cantidad):
                print("Stock retirado exitosamente.")
            else:
                print(
                    "Producto no encontrado o la cantidad es insuficiente.")
        except ValueError as ve:
            print(f"Error de valor: {ve}. Por favor, ingrese un valor válido.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}.")

    def calcular_valor_total_stock(self):
        instancia = producto.Producto()

        try:
            valor_total = instancia.calcular_total_stock()
            print(f"El valor total del stock es $: {valor_total:.2f} Pesos")
        except Exception as e:
            print(
                f"Error al calcular el valor total del stock: {e}.")

    def consultar_productos(self):
        try:
            nombre = input("Ingrese el nombre del producto a consultar: ")
            producto_info = self.instancia.consulta_producto(nombre)

            if producto_info:
                print("\nInformación del Producto:")
                print(f"Nombre: {nombre}")
                print(f"Descripción: {producto_info['descripcion']}")
                print(f"Precio: ${producto_info['precio']:.2f}")
                print(f"Stock: {producto_info['stock']}")
                print(f"Categoría: {producto_info['categoria']}")
            else:
                print("El producto no se encuentra registrado.")
        except Exception as e:
            print(f"Ha ocurrido un error al consultar el producto: {e}.")
