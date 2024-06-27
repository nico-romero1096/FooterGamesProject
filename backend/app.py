from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Root@localhost/footergames'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino las tablas
class Catalogo(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    fecha=db.Column(db.String(100))
    genero=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,fecha,genero,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.fecha=fecha
        self.genero=genero
        self.imagen=imagen




    #  si hay que crear mas tablas , se hace aqui




with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class CatalogoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','fecha','genero','imagen')




catalogo_schema=CatalogoSchema()            # El objeto producto_schema es para traer un producto
catalogos_schema=CatalogoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/catalogos',methods=['GET'])
def get_Catalogos():
    all_catalogos=Catalogo.query.all()         # el metodo query.all() lo hereda de db.Model
    result=catalogos_schema.dump(all_catalogos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/catalogos/<id>',methods=['GET'])
def get_catalogo(id):
    catalogo=Catalogo.query.get(id)
    return catalogo_schema.jsonify(catalogo)   # retorna el JSON de un producto recibido como parametro


@app.route('/catalogos/<id>',methods=['DELETE'])
def delete_catalogo(id):
    catalogo=Catalogo.query.get(id)
    db.session.delete(catalogo)
    db.session.commit()                     # confirma el delete
    return catalogo_schema.jsonify(catalogo) # me devuelve un json con el registro eliminado


@app.route('/catalogos', methods=['POST']) # crea ruta o endpoint
def create_catalogo():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    fecha=request.json['fecha']
    genero=request.json['genero']
    imagen=request.json['imagen']
    new_catalogo=Catalogo(nombre,fecha,genero,imagen)
    db.session.add(new_catalogo)
    db.session.commit() # confirma el alta
    return catalogo_schema.jsonify(new_catalogo)


@app.route('/catalogos/<id>' ,methods=['PUT'])
def update_catalogo(id):
    catalogo=Catalogo.query.get(id)
 
    catalogo.nombre=request.json['nombre']
    catalogo.fecha=request.json['fecha']
    catalogo.genero=request.json['genero']
    catalogo.imagen=request.json['imagen']


    db.session.commit()    # confirma el cambio
    return catalogo_schema.jsonify(catalogo)    # y retorna un json con el producto
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000