import os
import logging
from dotenv import load_dotenv
from healthcheck import HealthCheck
from app import create_app

# Configurar el registro de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación Flask
app = create_app()
app.app_context().push()

# Configuración del HealthCheck
health = HealthCheck()

# Función de verificación de salud
def app_working():
    return True, "App is working"

# Añadir la verificación de salud
health.add_check(app_working)

# Configurar el endpoint de healthcheck manualmente
app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())

# Ruta de prueba
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
