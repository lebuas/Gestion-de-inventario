import json
import os


class ControlDatos:
    def __init__(self, name_archivo_json):
        self.path_archivo_json = os.path.join(
            'src', 'database', name_archivo_json)
        self.diccionario_datos = {}

    def cargar_datos(self):
        with open(self.path_archivo_json, 'r') as file:
            datos = json.load(file)

        self.diccionario_datos = datos
        return self.diccionario_datos

    def actualizar_datos(self, diccionario_actualizado):
        with open(self.path_archivo_json, 'w') as file:
            json.dump(diccionario_actualizado, file, indent=4)
