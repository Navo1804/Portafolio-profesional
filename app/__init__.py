from flask import Flask
from flask_mail import Mail
from app.config import Config

mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    # Blueprint principal (todas las secciones del portafolio)
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

    # Páginas de error con el diseño del sitio
    from app.errores import registrar_errores
    registrar_errores(app)

    return app
