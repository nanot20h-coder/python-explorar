# ClassroomHub

## Descripción

ClassroomHub es una aplicación web desarrollada con Django como parte de los laboratorios de aprendizaje de Python. Permite consultar recursos educativos organizados por categorías y administrar su información mediante una base de datos MySQL.

## Funcionalidades

- Página principal con un mensaje de bienvenida.
- Catálogo público de recursos educativos.
- Organización de recursos mediante categorías.
- Visualización del título, descripción, categoría y disponibilidad de cada recurso.
- Administración de categorías y recursos mediante Django Admin.
- Persistencia de datos mediante MySQL.
- Operaciones CRUD utilizando el ORM de Django.
- Consultas mediante `all()`, `filter()`, `get()` y `select_related()`.
- Acceso a recursos relacionados mediante `related_name`.
- Protección de categorías con recursos asociados mediante `on_delete=models.PROTECT`.
- Navegación entre páginas y respuesta 404 para rutas inexistentes.
- Pruebas automatizadas para páginas, modelos y relaciones.

## Tecnologías utilizadas

- Python 3.14.8
- Django 6.1.3
- MySQL 26.7
- mysqlclient 2.3.1
- python-dotenv 1.2.4
- HTML

## Requisitos previos

- Python instalado.
- MySQL Server instalado y en funcionamiento.
- Git (opcional, para gestionar el repositorio).

## Instalación y configuración

### 1. Clonar o descargar el proyecto

Clonar el repositorio o descargar el proyecto y ubicarse en la carpeta `ClassroomHub`.

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

**Importante:** El archivo `.env` contiene información privada y no debe subirse al repositorio. Se utiliza `.env.example` como plantilla de configuración.

### 6. Ejecutar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

Las migraciones principales del proyecto son:

- `0001_initial`: creación de los modelos Category y Resource.
- `0002_resource_resource_type`: incorporación del campo `resource_type` al modelo Resource, conservando los registros existentes mediante un valor predeterminado.

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

- `name`: nombre de la categoría, único.
- `description`: descripción de la categoría.

### Resource

Representa los recursos educativos disponibles.

- `title`: título del recurso.
- `resource_type`: tipo de recurso, con valor predeterminado `General`.
- `description`: descripción del recurso.
- `available`: indica si está disponible.
- `category`: relación con el modelo Category mediante una clave foránea.
- `created_at`: fecha de creación del recurso.

### Relación entre modelos

La relación entre Category y Resource es de uno a muchos: una categoría puede tener varios recursos y


## Authentication and permissions

ClassroomHub uses Django authentication to manage user registration, login and logout.

### Available routes
- `/accounts/signup/`: Create an account.
- `/accounts/login/`: Log in.
- `/accounts/logout/`: Log out.
- `/dashboard/`: Private dashboard.
- `/resources/`: Public resource catalog.
- `/resources/review/`: Authorized resource review.

### Groups and permissions
The project includes the `Catalog reviewers` group with the `pages.view_resource` permission.

Users in this group can access the review page without Django Admin privileges.

### Session management
The dashboard displays the authenticated user's username and counts visits during the current session.

### Automated tests
Run the following commands:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test pages
```

The project includes 30 automated tests covering pages, models, authentication, sessions and permissions.

### Security
- Django manages password hashing.
- Registration creates regular users.
- Logout uses POST and CSRF protection.
- Permissions are verified on the server.
- Database credentials remain in `.env`.
