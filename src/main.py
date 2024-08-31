from models import consultas
from models import dataBase
from models import gestion
from models import registros
from models import stock


class Menu:

    def agregar_producto(self):
        _nombre = input("Ingrese el nombre del producto: ")
        _descripcion = input("Ingrese la descripción del producto: ")
        _precio = float(input("Ingrese el precio del producto: "))
        _stock = int(input("Ingrese el stock del producto: "))
        _categoria = input("Ingrese la categoría del producto: ")

        objeto = registros.Registros()
        new_objet = objeto.registrar_productos(_nombre, _descripcion,
                                               _precio, _stock, _categoria)

        guardar = dataBase.DataBase(new_objet, "productos.json", "productos")
        if guardar:
            print("Producto agregado")

    def agregar_categoria(self):
        _nombre = input("Ingrese el nombre de la categoría: ")
        _descripcion = input("Ingrese la descripción de la categoría: ")

        registros.Registros.registrar_categorias(_nombre, _descripcion)

    def agregar_proveedor(self):
        _nombre = input("Ingrese el nombre del  proveedor: ")
        _direccion = input("Ingrese la dirección del proveedor: ")
        _telefono = input("Ingrese el teléfono del proveedor: ")
        _productos = input("Ingrese los producto: ")

        registros.Registros.registrar_proveedores(_nombre, _direccion,
                                                  _telefono, _productos)

    def agregar_bodega(self):
        _nombre = input("Ingrese el nombre de la bodega: ")
        _ubicacion = input("Ingrese la ubicación de la bodega: ")
        _capacidad = int(input("Ingrese la capacidad máxima de la bodega: "))
        _producto = [input("Ingresar nombre del producto: "),
                     int(input("Ingresar la cantida: "))
                     ]

        objeto = registros.Registros()
        new_objet = objeto.registrar_bodegas(_nombre, _ubicacion,
                                             _capacidad, _producto)

        guardar = dataBase.DataBase(new_objet, "bodegas.json", "bodegas")
        if guardar:
            print("Producto agregado")


agregar = Menu()
agregar.agregar_bodega()
