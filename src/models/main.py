from models import bodega
from models import categoria
from models import proveedor
from models import producto


def entrada(leyenda):
    codigo = input(" ")
    nombre = input(" ")
    productos = input(" ")
    descripcion = input(" ")
    precio = float(input(" "))
    stock = int(input(" "))
    categorias = input(" ")
    direccion = input(" ")
    telefono = input(" ")
    cantidad = int(input(" "))

    informacion = {
        "codigo": codigo,
        "nombre": nombre,
        "productos": productos.split(",") if productos else [],
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "categorias": categorias,
        "direccion": direccion,
        "telefono": telefono,
        "cantidad": cantidad
    }

    return informacion


# Ejemplo de uso
datos = entrada("producto")
print(datos)
