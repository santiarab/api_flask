# API-TASK

API de creacion de tareas.

## Requisitos

- Python 3.x
- Flask
- Cualquier otra dependencia que tu proyecto necesite

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/santiarab/api_flask.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd api_flask
    ```
3. Instala las dependencias usando pip:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Establece la variable de entorno para Flask:
    ```bash
    export FLASK_APP=run.py  # Para Linux/macOS
    set FLASK_APP=run.py  # Para Windows
    ```
2. Inicia la aplicación:
    ```bash
    flask run
    ```

3. Visita la aplicación en `http://127.0.0.1:5000`.

## Endpoints de la API

### `GET /tasks`
Lista todas las tareas.

### `POST /tasks`
Crea una nueva tarea. Ejemplo de cuerpo de la solicitud:

```json
{
  "title": "Nueva tarea",
  "description": "Descripción opcional"
}