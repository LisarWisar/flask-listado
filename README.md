## Instalación

Instrucciones sobre cómo instalar y configurar el proyecto.

1. Clona el repositorio:
    ```bash
    git clone <URL del repositorio>
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd <nombre del proyecto>
    ```
3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

Instrucciones sobre cómo hacer funcionar el contenedor de docker:

Docker build: docker-compose build --no-cache
Docker compose up: docker-compose up
Docker down: Docker-compose -f compose.yaml down

In case you get an Authentication error, it might be due to a problem setting the user password, for that case, use the following command on the powershell terminal:
docker exec python-flask-app-container bash -c "echo 'usuario:1234' | chpasswd"