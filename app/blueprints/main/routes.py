from flask import render_template, flash, redirect, url_for, current_app
from flask_mail import Message
from app import mail
from app.blueprints.main import main_bp
from app.blueprints.main.forms import ContactoForm


@main_bp.route('/')
def home():
    return render_template('main/home.html')


@main_bp.route('/sobre-mi')
def sobre_mi():
    return render_template('main/sobre_mi.html')


@main_bp.route('/estudios')
def estudios():
    return render_template('main/estudios.html')


@main_bp.route('/experiencia')
def experiencia():
    return render_template('main/experiencia.html')


@main_bp.route('/proyectos')
def proyectos():
    return render_template('main/proyectos.html')


@main_bp.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactoForm()

    if form.validate_on_submit():
        destino = current_app.config.get('MAIL_DESTINO')

        msg = Message(
            subject=f'Nuevo mensaje de contacto: {form.asunto.data}',
            recipients=[destino],
            reply_to=form.correo.data,
            body=(
                f'Nombre: {form.nombre.data}\n'
                f'Correo: {form.correo.data}\n\n'
                f'Mensaje:\n{form.mensaje.data}'
            )
        )

        try:
            mail.send(msg)
            flash('¡Tu mensaje fue enviado correctamente! Te responderé pronto.', 'success')
        except Exception:
            flash('Hubo un problema al enviar tu mensaje. Intenta de nuevo o contáctame directo.', 'danger')

        return redirect(url_for('main.contacto'))

    return render_template('main/contacto.html', form=form)
