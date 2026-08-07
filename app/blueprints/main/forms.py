from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    correo = StringField('Correo', validators=[DataRequired(), Email(), Length(max=120)])
    asunto = StringField('Asunto', validators=[DataRequired(), Length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[DataRequired(), Length(max=2000)])
    enviar = SubmitField('Enviar mensaje')
