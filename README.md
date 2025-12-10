Esta API RESTful fue desarrollada para gestionar información relacionada con procesos de mantención industrial. Permite administrar empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo.
El proyecto utiliza Django y Django REST Framework, entregando datos en formato JSON y aplicando autenticación por token.

Objetivo del proyecto

El propósito de esta API es ofrecer servicios seguros y estructurados que puedan ser consumidos por aplicaciones web o móviles.
El sistema permite consultar información sin autenticación y modificarla solo si el usuario está autenticado, de acuerdo con los requisitos de la asignatura.

Requerimientos técnicos

Python 3.10 o superior

Django 5.x

Django REST Framework

Django REST Framework Authtoken

Instalación de dependencias:

pip install -r requirements.txt

Cómo ejecutar el proyecto

Aplicar migraciones:

python manage.py migrate


Crear un usuario administrador:

python manage.py createsuperuser


Iniciar el servidor:

python manage.py runserver


El servidor quedará disponible en:

http://127.0.0.1:8000/

Autenticación

La API utiliza autenticación por token.
Para generar un token asociado a un usuario:

python manage.py drf_create_token <usuario>


El token debe enviarse en las solicitudes que modifican datos:

Authorization: Token <token_generado>

Reglas de acceso

Usuarios no autenticados: solo lectura (GET).

Usuarios autenticados: pueden crear, actualizar y eliminar registros.

Endpoint de prueba (estado de la API)
GET /api/status/


Respuesta esperada:

{"status": "API funcionando correctamente"}

Endpoints principales

Empresas

GET /api/companies/
POST /api/companies/


Equipos

GET /api/equipments/


Técnicos

GET /api/technicians/


Planes de mantención

GET /api/plans/


Órdenes de trabajo

GET /api/workorders/

Estructura del proyecto
mantencion_api/
 ├── mantencion_api/
 ├── core/
 │    ├── models.py
 │    ├── serializers.py
 │    ├── views.py
 │    ├── permissions.py
 │    ├── urls.py
 └── manage.py
