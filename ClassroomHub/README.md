 

# Proyecto integrador: ClassroomHub

## Descripción general

ClassroomHub es una aplicación web educativa desarrollada con Python y Django. Su objetivo es permitir la consulta y gestión de recursos de aprendizaje mediante una plataforma organizada, con autenticación de usuarios y control de permisos.

Durante los laboratorios 6, 7, 8 y 9 se desarrolló progresivamente la aplicación, incorporando nuevas funcionalidades y mejorando su estructura.

## Desarrollo de los laboratorios

### Laboratorio 06: Introducción al desarrollo web con Django

Se inició la construcción de ClassroomHub y se preparó el entorno de desarrollo.

Actividades realizadas:
- Creación y configuración del proyecto Django.
- Organización de la estructura del proyecto.
- Configuración del entorno virtual y las dependencias.
- Creación de la aplicación `pages`.
- Configuración de rutas y vistas.
- Creación de plantillas HTML.
- Desarrollo de las páginas principales: inicio, recursos y acerca de.

### Laboratorio 07: Base de datos y modelos

Se integró la base de datos MySQL para almacenar la información de los recursos educativos.

Actividades realizadas:
- Configuración de la conexión con MySQL.
- Creación de los modelos `Category` y `Resource`.
- Definición de campos y relaciones entre modelos.
- Ejecución de migraciones.
- Consulta de información mediante el ORM de Django.
- Administración de registros mediante Django Admin.

### Laboratorio 08: Autenticación y permisos

Se implementó un sistema de autenticación para controlar el acceso de los usuarios a la plataforma.

Actividades realizadas:
- Registro de usuarios.
- Inicio y cierre de sesión.
- Protección de páginas mediante autenticación.
- Implementación de sesiones y contador de visitas al panel.
- Creación del grupo `Catalog reviewers`.
- Asignación de permisos para consultar recursos.
- Protección de la sección de revisión.

### Laboratorio 09: Formularios y operaciones CRUD

Se ampliaron las funcionalidades de ClassroomHub mediante formularios y vistas basadas en clases.

Actividades realizadas:
- Creación del formulario `ResourceForm` mediante `ModelForm`.
- Validación de los datos ingresados.
- Implementación de vistas basadas en clases.
- Consulta de detalles de los recursos.
- Creación de recursos.
- Actualización de recursos existentes.
- Eliminación de recursos con confirmación.
- Implementación de permisos para crear, editar y eliminar.
- Creación del grupo `Catalog editors`.
- Desarrollo de pruebas automatizadas para comprobar las funcionalidades.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **Django:** framework para el desarrollo web.
- **MySQL:** sistema de gestión de bases de datos.
- **HTML:** estructura de las páginas web.
- **Git:** control de versiones.
- **GitHub:** almacenamiento y seguimiento del código fuente.

## Estructura general del proyecto

```text
ClassroomHub/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pages/
│   ├── migrations/
│   ├── templates/
│   │   └── pages/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── .gitignore
```

## Ejecución del proyecto

1. Clonar el repositorio.
2. Ingresar a la carpeta `ClassroomHub`.
3. Crear y activar el entorno virtual.
4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

5. Configurar la conexión a MySQL.
6. Ejecutar las migraciones:

```bash
python manage.py migrate
```

7. Iniciar el servidor:

```bash
python manage.py runserver
```

8. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Pruebas automatizadas

Para ejecutar las pruebas de la aplicación:

```bash
python manage.py test pages
```

**Resultado del laboratorio 09:** 40 pruebas ejecutadas correctamente, sin errores.

También se realizaron pruebas manuales para comprobar el funcionamiento de las operaciones de creación, consulta, edición y eliminación de recursos.

## Conclusión

El desarrollo de ClassroomHub permitió fortalecer los conocimientos en Python y Django, desde la configuración inicial de una aplicación web hasta la implementación de bases de datos, autenticación, permisos, formularios y operaciones CRUD.

Cada laboratorio permitió incorporar nuevas funcionalidades y mejorar progresivamente la aplicación, aplicando buenas prácticas de desarrollo y control de versiones.
