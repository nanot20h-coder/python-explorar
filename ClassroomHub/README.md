# ClassroomHub

## Descripción

ClassroomHub es un sitio web desarrollado con Django como parte de un laboratorio de aprendizaje. Su objetivo es practicar la creación de rutas, vistas y plantillas para mostrar información en diferentes páginas.

## Funcionalidades

- Página principal con un mensaje de bienvenida.
- Página para consultar recursos educativos.
- Página con información sobre el proyecto.
- Navegación entre las diferentes páginas.
- Visualización de la disponibilidad de los recursos.
- Respuesta 404 cuando se intenta acceder a una página que no existe.

## Tecnologías y versiones utilizadas

- Python 3.14.8
- Django 6.1.3
- HTML
- SQLite

## Crear y activar el entorno virtual

Desde la carpeta principal del proyecto, ejecutar:

```bash
py -m venv .venv
```

Para activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

## Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar el proyecto

Para comprobar la configuración:

```bash
python manage.py check
```

Para iniciar el servidor:

```bash
python manage.py runserver
```

Después, abrir en el navegador:

http://127.0.0.1:8000/

## Rutas públicas

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/resources/` | Lista de recursos educativos |
| `/about/` | Información sobre ClassroomHub |

## Ejecutar las pruebas

Para ejecutar las pruebas automatizadas de la aplicación `pages`:

```bash
python manage.py test pages
```

Las pruebas comprueban que las páginas respondan correctamente, que se muestre el contenido esperado, que utilicen la plantilla base y que las rutas inexistentes devuelvan un error 404.

## Funcionalidades que todavía no incluye

- Registro e inicio de sesión de usuarios.
- Base de datos para guardar recursos educativos.
- Crear, editar o eliminar recursos.
- Formularios para registrar información.
- Panel de administración personalizado.

Actualmente, los recursos se encuentran definidos directamente en el archivo `pages/views.py`, por lo que los cambios realizados por los usuarios no se guardan.

## Estructura del proyecto

```text
ClassroomHub/
├── config/
├── pages/
│   ├── migrations/
│   ├── templates/
│   │   └── pages/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```
