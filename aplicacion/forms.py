from flask_wtf import FlaskForm
from wtforms import Form, IntegerField,SelectField,SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed 

class formcalculadora(FlaskForm):                      
    num1=IntegerField("Número1",validators=[DataRequired("Tienes que introducir el dato")])
    num2=IntegerField("Número2",validators=[DataRequired("Tienes que introducir el dato")])
    operador=SelectField("Operador",choices=[("+","Sumar"),("-","Resta"),
                            ("*","Multiplicar"),("/","Dividir")])
    submit = SubmitField('Calcular')

class UploadPdfForm(FlaskForm):
    pdf= FileField("Selecciona Pdf:", 
                   validators=[
                    FileRequired("Por favor elija un archivo valido"),
                    FileAllowed (['pdf'],"Solo pdf")
                   ]
    )
    submit= SubmitField("Subir")