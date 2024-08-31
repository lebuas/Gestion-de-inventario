# Sistema de Gestión de Inventario: Leymar Buenaventura

## Diagrama uml
![diagramaUml](src/static/uml.png )


## Descripción
 **Sistema de Gestión de Inventario** es una aplicación diseñada para gestionar productos, categorías, proveedores y bodegas. Permite registrar y administrar estos elementos, gestionar el stock, y realizar consultas e informes relacionados con el inventario.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

   - **`database/`**: Contiene el archivo `datos.json` que almacena los datos del inventario.
   - **`main.py`**: Inicializa el paquete.
   - **`models/`**: Contiene los módulos que implementan la lógica del sistema:
  - **`cargarDatos.py`**: Módulo para cargar y guardar datos desde/hacia `da os.json`.
  - **`Consultas.py`**: Módulo para realizar consultas sobre productos, categorías, proveedores, y bodegas.
  - **`ProductosStock.py`**: Módulo para gestionar el stock de productos.
  - **`Registros.py`**: Módulo para registrar productos, categorías, proveedores, y bodegas.
  - **`RelacionesEntidades.py`**: Módulo para manejar las relaciones entre productos, categorías, proveedores, y bodegas.
- **`requirements.txt`**: Contiene las dependencias necesarias para el proyecto.

## Cómo Iniciar el Programa
1. **Clonar el repositorio**
   
Para ejecutar este programa, primero clonamos el repositorio usando git. Hay que tener git instalado y luego ejecutar este comando en la ruta donde queramos clonar el proeycto.
   ```bash
   git clone "link del repositorio sin la comillas"
   ```

4. **Crear el Entorno Virtual**

Hay que tener instalado venv, que es un entorno virtual para trabajar con python, si no lo tine, intalarlo con el siguiente comando.

  ```bash
   pip install venv
  ```


  Caudo ya este instalado, abra una terminal y navega al directorio del proyecto. Luego, crea un entorno virtual con el siguiente comando:

   ```bash
   python -m venv "Nombre del entorno virtual sin las comillas"
   ```
  
 Caundo cree el entorno virtual tiene que activarlo par intalar los requerimintos. Buscar en entorno virtual y activarlo
  ```bash
  nombre_del_entorno\Scripts\activate
  ```
Una vez este activado el entorno virtual, se instalan los requerimienotos para correr el programa.
    ```bash
     pip install -r requirements.txt
    ```
Cuando se hayan instalado los requerimienos, ya podemos iniciar el programa. vamos a la carpeta src y abrimos el archivo main.py con cualquier editor y lo ejecutamos o des la terminal, buscamos le archiv main.py en la carpeta src y udamoa el comando:
    ```bash
   python main.py
     ```bash

# Sistema de Gestión de Inventario

##Nombre Leymar Buenaventura


## Diagrama uml:

## Descripción
 **Sistema de Gestión de Inventario** es una aplicación diseñada para gestionar productos, categorías, proveedores y bodegas. Permite registrar y administrar estos elementos, gestionar el stock, y realizar consultas e informes relacionados con el inventario.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

   - **`database/`**: Contiene el archivo `datos.json` que almacena los datos del inventario.
   - **`main.py`**: Inicializa el paquete.
   - **`models/`**: Contiene los módulos que implementan la lógica del sistema:
  - **`dataBase.py`**: Módulo para cargar y guardar datos desde/hacia `datos.json`.
  - **`consultas.py`**: Módulo para realizar consultas sobre productos, categorías, proveedores, y bodegas.
  - **`stock.py`**: Módulo para gestionar el stock de productos.
  - **`registros.py`**: Módulo para registrar productos, categorías, proveedores, y bodegas.
  - **`gestion.py`**: Módulo para manejar las relaciones entre productos, categorías, proveedores, y bodegas.
- **`requirements.txt`**: Contiene las dependencias necesarias para el proyecto.

## Cómo Iniciar el Programa

1. **Crear el Entorno Virtual**

Cuando ya esté instalado, abre una terminal y navega al directorio del proyecto. Luego, crea un entorno virtual con el siguiente comando:

    python -m venv "Nombre del entorno virtual sin las comillas"
   

Cuando hayas creado el entorno virtual, debes activarlo para instalar los requerimientos. Busca el entorno virtual y actívalo:

   ```bash
   Nombre_del_entorno_virtual\Scripts\activate
   ```
Una vez este activado el entonro virtual, se instalan los requerimienotos para correr el programa
     ```bash
     pip install -r requirements.txt
     ```
Cuando se hayan indtalado los requerimienos, ya podemos iniciar el programa. vamos a la carpeta src y abrimos el archivo main.py con cualquier editor y lo ejecutamos o des la terminal, 
buscamos le archiv main.py en la carpeta src y udamoa el comando:
     ```bash
     python main.py
     ```

