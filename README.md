Python Explorer - Laboratorios

Descripción

Repositorio personal para el desarrollo de los cuatro laboratorios de Python 

Este proyecto tiene como propósito fortalecer los fundamentos de programación mediante ejercicios prácticos y actividades integradoras.

Objetivos

Aplicar variables y tipos de datos.

Utilizar operadores aritméticos y conversiones de tipos.

Recibir y validar información ingresada por el usuario.

Desarrollar programas de consola en Python.

Practicar el control de versiones con Git y GitHub.

Estructura del repositorio

laboratorio-01/: ejercicios de fundamentos de Python y cotizador de compra.

laboratorio-02/: ejercicios de estructuras de control, colecciones y gestor de inventario.

laboratorio-03/:

laboratorio-04/: 

Laboratorio 01: Fundamentos de Python

El primer laboratorio trabaja con variables, tipos de datos, operadores, conversiones y entrada de información.

Actividad integradora: Cotizador de compra

El archivo cotizador_compra.py contiene una aplicación de consola que solicita los datos de un cliente y un producto, y calcula:

Subtotal de la compra.

Valor del descuento.

Base después del descuento.

Valor del impuesto.

Total final.

También se trabaja en la validación de entradas para controlar datos incorrectos.

Requisitos

Python 3.

Visual Studio Code o un editor de código equivalente.

Instrucciones de ejecución

Clonar o descargar el repositorio.

Abrir la carpeta del proyecto en Visual Studio Code.

Abrir una terminal dentro de laboratorio-01.

Ejecutar:

python cotizador_compra.py

En Windows también se puede utilizar:

py cotizador_compra.py

Ingresar los datos solicitados y revisar el resumen de compra.

Control de versiones

Los cambios se registran mediante commits descriptivos en GitHub para documentar el desarrollo de los ejercicios, las correcciones y las mejoras realizadas.

Estado del proyecto

El repositorio se actualizará progresivamente durante los cuatro laboratorios. Las actividades se marcarán como completadas una vez que hayan sido desarrolladas y verificadas.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Laboratorio 02: Estructuras de Control y Colecciones
El segundo laboratorio trabaja con condiciones (if, elif, else), ciclos (for, while), listas, tuplas, conjuntos, diccionarios y comprensiones de colecciones.

Actividad integradora: Gestor de inventario
El archivo gestor_inventario.py contiene una aplicación de consola con un menú interactivo que permite administrar productos en memoria mediante una lista de diccionarios y ofrece las siguientes funciones:

Registrar nuevos productos validando datos correctos.

Listar todos los productos registrados en el sistema.

Buscar un producto por su código.

Actualizar el precio o la cantidad de un producto existente.

Eliminar productos del inventario.

Consultar productos sin existencias y ver un reporte general con unidades totales, valor económico acumulado y categorías utilizadas.

También se implementan validaciones para rechazar códigos duplicados, categorías no permitidas, precios no positivos y cantidades negativas.

Requisitos
Python 3.

Visual Studio Code o un editor de código equivalente.

Instrucciones de ejecución
Abrir la carpeta del proyecto en Visual Studio Code.

Abrir una terminal dentro de laboratorio-02.

Ejecutar:

Bash
python gestor_inventario.py
En Windows también se puede utilizar:

DOS
py gestor_inventario.py
Seleccionar la opción deseada del menú interactivo para gestionar el inventario.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Laboratorio 03: Funciones, Módulos y Programación Orientada a Objetos

El tercer laboratorio trabaja con funciones, módulos, clases, objetos, encapsulamiento, propiedades, validaciones y colaboración entre objetos.

Actividad integradora: Gestor de inventario de Novexa

El proyecto integrador se encuentra en la carpeta laboratorio-03/gestor_inventario/ y está orientado a la administración de recursos digitales relacionados con el diseño y la identidad visual de una empresa.

El proyecto utiliza programación orientada a objetos para representar los productos y administrar el inventario, separando la lógica de negocio de la interacción con el usuario.

Las funcionalidades del sistema incluyen:

Registrar recursos digitales.

Consultar y listar los recursos registrados.

Buscar recursos por su nombre.

Actualizar la información de un recurso.

Eliminar recursos del inventario.

Generar informes generales del inventario.

Validar los datos ingresados por el usuario.

Los recursos pueden representar logotipos, plantillas, paletas de colores, manuales de marca y otros elementos digitales.

Estructura del proyecto

Dentro de laboratorio-03/gestor_inventario/ se encuentran los siguientes archivos:

producto.py: define la clase Producto y las validaciones relacionadas con los datos de cada recurso.

inventario.py: administra los productos y contiene la lógica de negocio del inventario.

main.py: contiene la interacción con el usuario y el menú principal de la aplicación.

README.md: contiene información específica sobre el proyecto integrador.

Instrucciones de ejecución

Importante: para ejecutar el proyecto, debes ingresar a la carpeta gestor_inventario, ya que allí se encuentra el archivo main.py.

Abrir la carpeta principal del repositorio en Visual Studio Code.

Abrir una terminal.

Ingresar a la carpeta del proyecto:

cd laboratorio-03/gestor_inventario

Ejecutar la aplicación:

python main.py

En Windows también se puede utilizar:

py main.py

Utilizar el menú interactivo para seleccionar la operación que se desea realizar.

Nota: los datos se mantienen en memoria mientras la aplicación está en ejecución. Al cerrar el programa, los datos registrados no se conservan, salvo que se implemente un mecanismo de almacenamiento persistente.

Control de versiones
Los cambios se registran mediante commits descriptivos en GitHub para documentar el desarrollo de los ejercicios, las correcciones y las mejoras realizadas.

Estado del proyecto
El repositorio se actualizará progresivamente durante los cuatro laboratorios. Las actividades se marcarán como completadas una vez que hayan sido desarrolladas y verificadas.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Explorador de Python - Laboratorios

## Descripción

Este repositorio contiene las actividades y proyectos que he desarrollado durante mi aprendizaje de Python en el programa Tecnólogo en Análisis y Desarrollo de Software (ADSO) del SENA.

A través de los laboratorios he practicado diferentes conceptos de programación, comenzando por los fundamentos del lenguaje y avanzando hacia la programación orientada a objetos, el manejo de archivos y la generación de reportes.

Cada laboratorio me ha permitido aprender nuevos conceptos y aplicarlos en pequeños proyectos.

## Contenido del repositorio

### Laboratorio 01 - Fundamentos de Python

En este laboratorio trabajé con los conceptos básicos de Python, como variables, tipos de datos, operadores, conversiones y entradas de información.

**Proyecto:** Cotizador de compra.

### Laboratorio 02 - Condiciones, ciclos y colecciones

En este laboratorio practiqué el uso de condiciones, ciclos y colecciones como listas, tuplas, conjuntos y diccionarios.

También desarrollé un gestor de inventario con opciones para registrar, consultar, buscar, actualizar, eliminar y filtrar productos.

**Proyecto:** Gestor de inventario básico.

### Laboratorio 03 - Funciones, módulos y programación orientada a objetos

En este laboratorio organicé el código utilizando funciones, módulos, clases y objetos. También trabajé con validaciones y con la separación de responsabilidades entre los diferentes archivos del proyecto.

**Proyecto:** Gestor de inventario organizado mediante clases y módulos.

### Laboratorio 04 - Archivos, persistencia y reportes

En este laboratorio amplié el gestor de inventario para guardar y recuperar los productos mediante archivos JSON. También agregué el manejo de errores y la exportación de reportes en formato CSV.

**Proyecto:** Gestor de inventario persistente de Novexa.

## Estructura del repositorio

```text
Explorador de Python - Laboratorios/
├── README.md
├── laboratorio-01/
│   ├── README.md
│   └── cotizador_compra.py
├── laboratorio-02/
│   ├── README.md
│   └── gestor_inventario.py
├── laboratorio-03/
│   ├── README.md
│   └── gestor_inventario/
└── laboratorio-04/
    ├── README.md
    └── gestor_inventario/
```

La estructura muestra la organización general del repositorio. Dentro de cada laboratorio se encuentran los archivos y carpetas correspondientes a sus actividades.

## Tecnologías y herramientas

- **Python:** lenguaje utilizado para desarrollar los ejercicios y proyectos.
- **Visual Studio Code:** editor utilizado para escribir y ejecutar el código.
- **Git:** herramienta utilizada para registrar los cambios realizados.
- **GitHub:** plataforma donde se almacena el repositorio y se puede consultar la evolución de los proyectos.
- **JSON y CSV:** formatos utilizados en el Laboratorio 04 para guardar y exportar información.

## Aprendizajes generales

Durante el desarrollo de estos laboratorios he aprendido a trabajar con diferentes estructuras de Python, organizar el código en funciones y clases, validar información y utilizar archivos para guardar datos.

También he practicado la identificación y corrección de errores y el uso de Git y GitHub para llevar un seguimiento de los cambios.

Cada laboratorio representa un avance en mi proceso de aprendizaje y me ha permitido construir proyectos cada vez más completos.



**Repositorio:** https://github.com/nanot20h-coder/python-explorar.git

