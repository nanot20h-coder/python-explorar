# ClassroomHub

## Descripción

ClassroomHub es una aplicación web desarrollada con Django como parte de los laboratorios de aprendizaje de Python. Permite consultar recursos educativos organizados por categorías y administrar su información mediante una base de datos MySQL.

## Funcionalidades

- Página principal con un mensaje de bienvenida.
- Catálogo público de recursos educativos.
- Organización de recursos mediante categorías.
- Visualización de la descripción y disponibilidad de cada recurso.
- Panel de administración de Django para gestionar categorías y recursos.
- Persistencia de datos mediante MySQL.
- Operaciones CRUD utilizando el ORM de Django.
- Navegación entre páginas y respuesta 404 para rutas inexistentes.
- Pruebas automatizadas para páginas y modelos.

## Tecnologías utilizadas

- Python 3.14.8
- Django 6.1.3
- MySQL
- mysqlclient 2.3.1
- python-dotenv 1.2.4
- HTML

## Requisitos previos

- Python instalado.
- MySQL Server instalado y en funcionamiento.
- Git (opcional, para gestionar el repositorio).

## Instalación y configuración

### 1. Clonar o descargar el proyecto

Ubicarse en la carpeta del proyecto ClassroomHub.

### 2. Crear y activar el entorno virtual

En Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 4. Crear la base de datos MySQL

Desde MySQL, ejecutar:

```sql
CREATE DATABASE classroom_hub
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Crear un usuario para la aplicación y asignarle permisos:

```sql
CREATE USER 'classroomhub_user'@'127.0.0.1'
IDENTIFIED BY 'tu_contraseña_segura';

GRANT ALL PRIVILEGES ON classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';

GRANT ALL PRIVILEGES ON test_classroom_hub.*
TO 'classroomhub_user'@'127.0.0.1';

FLUSH PRIVILEGES;
```

### 5. Configurar las variables de entorno

Crear una copia de `.env.example` con el nombre `.env`:

```bash
copy .env.example .env
```

Configurar las siguientes variables dentro del archivo `.env`:

```env
DB_NAME=classroom_hub
DB_USER=classroomhub_user
DB_PASSWORD=tu_contraseña_segura
DB_HOST=127.0.0.1
DB_PORT=3306
```

Reemplazar `tu_contraseña_segura` por la contraseña configurada para el usuario de MySQL.

**Importante:** el archivo `.env` contiene información privada y no debe subirse al repositorio. Se utiliza `.env.example` como plantilla.

### 6. Ejecutar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Seguir las instrucciones para configurar el usuario y la contraseña.

## Ejecutar el proyecto

Comprobar la configuración:

```bash
python manage.py check
```

Iniciar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Página principal |
| `/resources/` | Catálogo de recursos educativos |
| `/about/` | Información del proyecto |
| `/admin/` | Panel de administración de Django |

## Modelos de datos

### Category

Representa las categorías de los recursos educativos.

- `name`: nombre de la categoría.
- `description`: descripción de la categoría.

### Resource

Representa los recursos educativos disponibles.

- `title`: título del recurso.
- `description`: descripción del recurso.
- `available`: indica si está disponible.
- `category`: relación con el modelo Category.
- `created_at`: fecha de creación.

## Operaciones CRUD con el ORM

La aplicación permite trabajar con los registros mediante el ORM de Django:

- **Create:** crear categorías y recursos.
- **Read:** consultar categorías y recursos.
- **Update:** actualizar información de los registros.
- **Delete:** eliminar registros.

## Ejecutar las pruebas

Para ejecutar las pruebas automatizadas:

```bash
python manage.py test pages -v 2
```

Las pruebas verifican el funcionamiento de las páginas, el catálogo de recursos, los modelos, la representación de los objetos y la disponibilidad predeterminada de los recursos.

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
├── .env
├── .env.example
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Autoría

Proyecto desarrollado como práctica de aprendizaje de Python, Django y persistencia de datos con MySQL.