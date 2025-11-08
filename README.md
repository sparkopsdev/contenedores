# 🧩 Person API

API REST desarrollada en **FastAPI** y **PostgreSQL** para la gestión de personas.

---

## 🚀 Descripción del proyecto

Este proyecto define un servicio `personAPI` con una estructura modular en Python (FastAPI + SQLAlchemy), capaz de persistir y recuperar entidades de tipo **Persona** en una base de datos PostgreSQL.

Cada persona tiene los siguientes campos:

| Campo | Descripción |
|--------|--------------|
| `id` | Clave primaria (PK) |
| `firstName` | Nombre |
| `lastName` | Apellidos |
| `dni` | Documento Nacional de Identidad |
| `birthProvince` | Provincia de nacimiento |

### 🧾 Endpoints disponibles
| Método   | Endpoint       | Descripción                                                                         | Ejemplo de cuerpo (POST)                                                                               |
| :------- | :------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| `GET`    | `/person`      | Lista todas las personas almacenadas. Si la lista está vacía, devuelve error `404`. | —                                                                                                      |
| `GET`    | `/person/{id}` | Recupera una persona específica por su ID.                                          | —                                                                                                      |
| `POST`   | `/person`      | Crea una nueva persona en la base de datos.                                         | `json { "firstName": "Ana", "lastName": "García", "dni": "12345678A", "birthProvince": "Madrid" } ` |
| `DELETE` | `/person/{id}` | Elimina la persona con el ID indicado.                                              | —                                                                                                      |

---

## Modos de ejecución:

### Local

Para ejecutar el stack en local, debe de haber un servidor *PostgreSQL* escuchando en el puerto `5432` del equipo y una base de datos llamada *person_db* creada en él. Después, se tiene que modificar el archivo `.env` tal que:

```sh
# Database configuration:

DB_HOST=localhost
DB_USER=<usuario-de-la-db>
DB_PASSWORD=<contraseña-de-la-db>
DB_NAME=person_db

# API configuration:

API_SERVER=localhost
API_PORT=8000
DEBUG=True
```

Una vez hecho esto, ejecutar:

```sh
python -m venv venv
# Si se ejecuta desde Windows:
.\venv\Scripts\activate
# Si tu entorno es MacOS/Linux:
source venv\bin\activate

pip install -r requirements.txt
python runserver.py
python apitester.py
```

### Docker

Para la ejecución en Docker, dejar el .env como viene por default en el repositorio y después:

```sh
docker compose up --build # "-d" opcional para no mostrar la salida

pip install requests

python apitester.py
```

