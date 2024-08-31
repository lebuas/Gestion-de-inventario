from models import dataBase


class Stock:

    def agregar_productos(self, nombre, cantidad):
        stock = {
            "producto": nombre,
            cantidad: cantidad
        }
        agregar = dataBase.DataBase(stock, "stock.json", stock)
        if agregar:
            print("se agrego el stock")

    def retirar_productos(self,):
        pass

    def calcular_total_stock(self):
        pass
