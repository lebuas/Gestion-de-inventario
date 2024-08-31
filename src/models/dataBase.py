
import json
import os


class DataBase:
    def __init__(self, objeto, archivo, modelo):
        self.modelo = modelo
        self.archivo_json = os.path.join('database', archivo)
        self.objeto = objeto

        self.cargar_datos()

    def cargar_datos(self):
        with open(self.archivo_json, 'r') as file:
            datos = json.load(file)

        self.base_datos = datos

        self.agregar_objeto()

    def agregar_objeto(self):
        if self.modelo in self.base_datos:
            self.base_datos[self.modelo].append(self.objeto)
        else:
            self.base_datos[self.modelo] = [self.objeto]
        print(self.base_datos)
        self.guardar_datos()

    def guardar_datos(self):
        # Guardar los datos actualizados en el archivo JSON
        with open(self.archivo_json, 'w') as file:
            json.dump(self.base_datos, file, indent=4)

    def get_productos(self):
        pass

    def get_categorias(self):
        pass

    def get_proveedores(self):
        pass

    def get_bodegas(self):
        pass
