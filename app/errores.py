from flask import render_template


def registrar_errores(app):
    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return render_template('errores/error.html',
                                codigo=404,
                                mensaje='Página no encontrada'), 404

    @app.errorhandler(500)
    def error_interno(error):
        return render_template('errores/error.html',
                                codigo=500,
                                mensaje='Ocurrió un error interno'), 500
