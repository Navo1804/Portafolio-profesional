import os
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-de-desarrollo-no-usar-en-produccion')

    # Configuración del correo (Flask-Mail)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')

    # Correo donde quieres recibir los mensajes del formulario de contacto
    MAIL_DESTINO = os.environ.get('MAIL_DESTINO')

    # Datos para los botones de contacto directo
    TELEFONO_CONTACTO = os.environ.get('TELEFONO_CONTACTO', '')
    WHATSAPP_NUMERO = os.environ.get('WHATSAPP_NUMERO', '')
