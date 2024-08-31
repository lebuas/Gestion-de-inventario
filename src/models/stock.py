from models import dataBase


class Stock:

    def agregar_productos(self, producto, cantidad):
        stock = {
            "producto": producto,
            cantidad: cantidad
        }
        agregar = dataBase.DataBase(stock, "stock.json", stock)
        if agregar:
            print("se agrego el stock")

    def retirar_productos(self, base_datos, producto, cantidad):
        if base_datos[producto] >= cantidad:
            continue
        else:

    def calcular_total_stock(self):
        pass
