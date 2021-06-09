from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import RadioField,StringField,IntegerField,SelectField,BooleanField,SubmitField,FieldList,FormField,TextAreaField,MultipleFileField
from wtforms.validators import DataRequired,InputRequired,EqualTo,Optional,Length
# from forex_python.converter import CurrencyRates
# c = CurrencyRates()
    #######################
class ComfortForm(FlaskForm):
    agua_caliente = BooleanField('Agua caliente')
    aire_acondicionado = BooleanField('Aire acondicionado')
    altillo = BooleanField('Altillo')
    amueblada = BooleanField('Amueblada')
    balcón = BooleanField('Balcón')
    barbacoa = BooleanField('Barbacoa')
    box = BooleanField('Box')
    bungalow = BooleanField('Bungalow')
    calefacción = BooleanField('Calefacción')
    depósito = BooleanField('Depósito')
    dormitorio_de_servicio = BooleanField('Dormitorio de servicio')
    estufa_leña = BooleanField('Estufa leña')
    garaje = BooleanField('Garaje')
    gas_por_cañería = BooleanField('Gas por cañería')
    gym = BooleanField('Gym')
    instalación_de_tv_cable = BooleanField('Instalación de tv cable')
    jacuzzi = BooleanField('Jacuzzi')
    jardín = BooleanField('Jardín')
    lavadero = BooleanField('Lavadero')
    lavandería = BooleanField('Lavandería')
    linea_blanca = BooleanField('Linea blanca')
    living_comedor = BooleanField('Living comedor')
    losa_radiante = BooleanField('Losa radiante')
    parrillero = BooleanField('Parrillero')
    patio = BooleanField('Patio')
    piscina = BooleanField('Piscina')
    piso_porcelanato = BooleanField('Piso porcelanato')
    placard_en_la_cocina = BooleanField('Placard en la cocina')
    placard_en_dormitorio = BooleanField('Placard en dormitorio')
    playroom = BooleanField('Playroom')
    previsión_aa = BooleanField('Previsión aa')
    sauna = BooleanField('Sauna')
    sótano = BooleanField('Sótano')
    terraza = BooleanField('Terraza')
    terraza_lavadero = BooleanField('Terraza lavadero')
    vestidor = BooleanField('Vestidor')
    vista_al_mar = BooleanField('Vista al mar')
    walkin_closet = BooleanField('Walk-in closet')
    wifi = BooleanField('Wifi')
    
    ###############
class SeguridadForm(FlaskForm):
    alarma = BooleanField('Alarma')
    cámaras_cctv = BooleanField('Camaras cctv')
    cerca_perimetral = BooleanField('Cerca perimetral')
    portería_24hs = BooleanField('Porteria 24hrs')
    portón_eléctrico = BooleanField('Porton electrico')
    rejas = BooleanField('Rejas')
    guardia_de_seguridad = BooleanField('Guardia de seguridad')


class PropertyForm(FlaskForm):
    precio_pesos = IntegerField('Pesos',validators=[Optional()])
    precio_dolares = IntegerField('Dolares',validators=[Optional()])   
    ref = StringField('Ref', validators=[InputRequired(),Length(max=5, message='Demasiado largo')])
    metraje_edificio = IntegerField('Metraje de Planta',validators=[DataRequired(message = ('Valor no valido'))])
    metraje_patio = IntegerField('Metraje Patio',validators=[Optional()])
    titulo = StringField('Titulo', validators=[DataRequired(message = ('Valor no valido')),Length(max=50, message='Demasiado largo')])
    nombre = StringField('Nombre', validators=[DataRequired(message = ('Valor no valido'))])
    apellido = StringField('Apellido', validators=[DataRequired(message = ('Valor no valido'))])
    email = StringField('Email', validators=[DataRequired(message = ('Valor no valido'))])
    telefono = IntegerField('Telefono',validators=[DataRequired(message = ('Valor no valido'))])
    operacion = SelectField('Operacion',choices=['Venta','Alquiler'],validators=[DataRequired()])
    tipo_propiedad = SelectField('Propiedad',choices=['Casa','Apartamento','Oficina', 'Terreno', 'Local', 'Depósito'],validators=[DataRequired()])
    barrio = SelectField('Barrio',choices=['Aguada','Aires Puros','Arroyo Seco','Atahualpa','Bañados de Carrasco','Barra de Carrasco','Barrio Sur','Bella Italia','Bella Vista','Belvedere','Bolivar','Brazo Oriental','Buceo','Camino Maldonado','Capurro','Capurro Bella Vista','Carrasco','Carrasco Barrios con seguridad privada','Carrasco Este','Carrasco Norte','Casabó','Casabó Pajas Blancas','Casavalle','Centro','Cerrito','Cerro','Ciudad Vieja','Colón','Conciliación','Cordón','Flor de maroñas','Goes','Golf','Ituzango','Jacinto Vera','Jardines del Hipódromo','La Blanqueada','La Caleta','La Colorada','La Comercial','La Figurita ','La Paloma Tomkinson','La Teja','Larrañaga','Las Acacias','Las Canteras','Lezica','Malvín ','Malvín Norte','Manga ','Marconi','Maroñas','Melilla','Mercado Modelo','Montevideo (en general)','Nuevo Paris','Pajas Blancas','Palermo','Parque Batlle','Parque Miramar','Parque Rodó','Paso de la Arena','Paso Molino','Peñarol','Peñarol Lavalleja','Perez Castellanos ','Piedras Blancas','Pocitos','Pocitos Nuevo','Prado','Prado Nueva Savona','Puerto','Puerto Buceo','Punta Carretas','Punta Espinillo','Punta Gorda','Punta de Rieles','Reducto','Santiago Vazquez','Sayago','Tres Cruces','Tres Ombues','Unión','Villa Biattitz','Villa Dolores','Villa Española','Villa Garcia Manga Rural','Villa Muñoz','Zona Rural'],validators=[DataRequired()])
    baños = SelectField('Baños',choices=['1','2','3+'],validators=[DataRequired()])
    direccion = StringField('Direccion',validators=[Optional()])
    dormitorios = SelectField('Dormitorios',choices=['No','1','2','3','4','5+'],validators=[DataRequired()])
    descripcion = TextAreaField('Descripcion', validators=[InputRequired(),Length(max=2000, message='Demasiado largo')],render_kw={"rows": 10, "cols": 50})
    permuta = RadioField('Permuta',coerce=int,choices=[(0,'No'),(1,'Si'),(2,'Preguntar')],validators=[Optional()])
    financia = RadioField('Financia',coerce=int,choices=[(0,'No'),(1,'Si'),(2,'Preguntar')],validators=[Optional()])
    destacado = BooleanField('Destacado')
    sobre = SelectField('Sobre', choices=['No aplica','Avenida','Rambla','Otros'],validators=[Optional()])
    distancia_al_mar = IntegerField('Distancia al Mar',validators=[Optional()])
    gastos_comunes = IntegerField('Gastos Comunes',validators=[Optional()])
    garaje = SelectField('Garaje',choices=['0','1','2','3+'],validators=[DataRequired()])
    estado = SelectField('Estado',choices=['Reciclada','A reciclar','Requiere mantenimiento','Buen estado','Excelente estado','A estrenar','En construcción'],validators=[DataRequired()])
    orientacion = SelectField('Orientacion',choices=['N','S','E','W'],validators=[DataRequired()])
    disposicion = SelectField('Disposicion',choices=['Frente','Inferior','Lateral','Contrafrente'],validators=[DataRequired()])
    n_plantas = SelectField('Numero de plantas',choices=['1','2','3','4','5+'],validators=[DataRequired()])
    comfort = FormField(ComfortForm)
    seguridad = FormField(SeguridadForm)
    fotos = MultipleFileField('Ingresar Fotos',validators=[FileAllowed(['.jpg','.png','.jpeg'],'Solo jpg, png, jpeg'),Optional()])
    submit = SubmitField('Ingresar')


    