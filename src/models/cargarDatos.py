import json


class ReadWriteJson:

    def __init__(self, archivo_db):
        self.archivo_db = archivo_db
        self.productos = {}
        self.categorias = {}
        self.proveedores = {}
        self.bodegas = {}
        self.cargar_datos()

    def cargar_datos(self):
        """Carga datos del archivo JSON en los diccionarios internos."""
        try:
            with open(self.archivo_db, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = {
                    p['nombre']: p for p in datos.get('productos', [])}
                self.categorias = {
                    c['nombre']: c for c in datos.get('categorias', [])}
                self.proveedores = {
                    p['nombre']: p for p in datos.get('proveedores', [])}
                self.bodegas = {
                    b['nombre']: b for b in datos.get('bodegas', [])}

        except FileNotFoundError:
            # El archivo no existe, se creará cuando se guarden los datos.
            pass
        except json.JSONDecodeError:
            print("El archivo json está vacío o tiene un formato incorrecto.")

    def guardar_datos(self):
        """Guarda los datos actuales en el archivo JSON."""
        datos = {
            'productos': list(self.productos.values()),
            'categorias': list(self.categorias.values()),
            'proveedores': list(self.proveedores.values()),
            'bodegas': list(self.bodegas.values())
        }
        with open(self.archivo_db, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    def get_productos(self):
        """Devuelve el diccionario de productos."""
        return self.productos

    def get_categorias(self):
        """Devuelve el diccionario de categorías."""
        return self.categorias

    def get_proveedores(self):
        """Devuelve el diccionario de proveedores."""
        return self.proveedores

    def get_bodegas(self):
        """Devuelve el diccionario de bodegas."""
        return self.bodegas
