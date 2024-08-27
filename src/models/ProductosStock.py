class Stock:
    def __init__(self):
        self.stock = {}  # Diccionario para almacenar el stock de productos

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def retirar_stock(self, producto, cantidad):
        if producto in self.stock:
            if self.stock[producto] >= cantidad:
                self.stock[producto] -= cantidad
                if self.stock[producto] == 0:
                    del self.stock[producto]
            else:
                raise ValueError(
                    f"No hay suficiente stock de '{producto}'para retirar {
                        cantidad}.")
        else:
            raise ValueError(f"El producto '{producto}' no está en el stock.")

    def calcular_valor_total_stock(self, precios):
        valor_total = 0
        for producto, cantidad in self.stock.items():
            if producto in precios:
                valor_total += cantidad * precios[producto]
            else:
                raise ValueError(
                    f"Precio no encontrado para el producto '{producto}'.")
        return valor_total
