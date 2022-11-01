from flask import Flask, request, jsonify
from flask_restful import Api 
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv
from xml.dom import minidom

from Clases.Categoria import Categoria
from Clases.Cliente import Cliente
from Clases.Configuracion import Configuracion
from Clases.Consumo import Consumo
from Clases.Instancia import Instancia
from Clases.Recurso import Recurso



app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv()

Categorias = [] #lista
Clientes = [] #lista
Recursos = [] #lista
Consumos =[] #lista

Configuraciones_glob = []
Instancias_glob=[]

#subir archivo Configuraciones en XML  -----
@app.route('/post-config', methods=['POST'])
def PostListaConfig():
    global Recursos
    global Categorias
    global Clientes
    global Configuraciones_glob
    global Instancias_glob
    
    #get xml info
    configuracion = request.json['data']
    #parse xml info
    config_files =  minidom.parseString(configuracion)
    
    #--recursos generales--
    
    listRecursos_gen = config_files.getElementsByTagName('listaRecursos')[0]
    recursos_list = listRecursos_gen.getElementsByTagName('recurso')
    count_recursos = 0
    for recurso_gen in recursos_list:
       count_recursos += 1
       id_recurso = recurso_gen.attributes['id'].value
       nombre = recurso_gen.getElementsByTagName('nombre')[0]
       abreviatura = recurso_gen.getElementsByTagName('abreviatura')[0]
       metrica = recurso_gen.getElementsByTagName('metrica')[0]
       tipo = recurso_gen.getElementsByTagName('tipo')[0]
       valorXhora = recurso_gen.getElementsByTagName('valorXhora')[0]
       new_Recurso = Recurso(id_recurso,nombre.firstChild.data,abreviatura.firstChild.data,metrica.firstChild.data,tipo.firstChild.data,valorXhora.firstChild.data)
       Recursos.append(new_Recurso)
    
    # -- categorias generales -- 
    listCateg_gen = config_files.getElementsByTagName('listaCategorias')[0]
    categorias = listCateg_gen.getElementsByTagName('categoria')
    count_categ = 0
    for cat in categorias:
        Configuraciones = [] #lista
        
        count_categ += 1
        id_categoria = cat.attributes['id'].value
        nombre_categoria = cat.getElementsByTagName('nombre')[0]
        descr_categoria = cat.getElementsByTagName('descripcion')[0]
        carga_de_trabajo = cat.getElementsByTagName('cargaTrabajo')[0]
        list_config = cat.getElementsByTagName('configuracion')

        #configuraciones por Categoria
        count_config = 0
        for config in list_config:
            count_config += 1
            id_config = config.attributes['id'].value
            nombre_config = config.getElementsByTagName('nombre')[0]
            dscr_config = config.getElementsByTagName('descripcion')[0]
            
            recursosCat = config.getElementsByTagName('recurso')
            #lista de recursos por configuracion (id's y cantidad)
            list_rec_config = []
            i=0
            for rec_config in recursosCat:
                id_recurso = rec_config.attributes['id'].value
                nodo = config.getElementsByTagName('recurso')[i]
                recursos ={
                    "id_recurso":id_recurso,
                    "cantidad":nodo.firstChild.data
                }
                i+=1
                list_rec_config.append(recursos)

            new_config = Configuracion(id_config,nombre_config.firstChild.data,dscr_config.firstChild.data,list_rec_config)
            Configuraciones.append(new_config)
            Configuraciones_glob.append(new_config)
            
        new_categoria = Categoria(id_categoria,nombre_categoria.firstChild.data,descr_categoria.firstChild.data,carga_de_trabajo.firstChild.data,Configuraciones)
        Categorias.append(new_categoria) 
    
    #clientes
    clientes = config_files.getElementsByTagName('cliente')
    count_clientes = 0 
    for clt in clientes:
        count_clientes += 1
        Instancias = [] #lista
        
        NIT = clt.attributes['nit'].value
        nombre_cliente = clt.getElementsByTagName('nombre')[0]
        usuario = clt.getElementsByTagName('usuario')[0]
        clave = clt.getElementsByTagName('clave')[0]
        direccion = clt.getElementsByTagName('direccion')[0]
        email = clt.getElementsByTagName('correoElectronico')[0]
        instancias = clt.getElementsByTagName('instancia')
        
        for ins in instancias:
            id_instance = ins.attributes['id'].value
            id_configuracion = ins.getElementsByTagName('idConfiguracion')[0]
            nombre = ins.getElementsByTagName('nombre')[0]
            fecha_inicio = ins.getElementsByTagName('fechaInicio')[0]
            estado = ins.getElementsByTagName('estado')[0]
            if estado.firstChild.data == 'Cancelada':
                fecha_finalOn = ins.getElementsByTagName('fechaFinal')[0]
                fecha_final = fecha_finalOn.firstChild.data
            else:
                fecha_final = '--'
            
            new_instancia = Instancia(id_instance,id_configuracion.firstChild.data,nombre.firstChild.data,fecha_inicio.firstChild.data,fecha_final,estado.firstChild.data)
            Instancias.append(new_instancia)
            Instancias_glob.append(new_instancia)
            
        new_cliente = Cliente(NIT,nombre_cliente.firstChild.data,usuario.firstChild.data,clave.firstChild.data,direccion.firstChild.data,email.firstChild.data,Instancias)
        Clientes.append(new_cliente)
            
    Dato ={
        'data': 'archivo obtenido',
        'recursos':str(count_recursos)+' recursos añadidos',
        'categorias':str(count_categ)+' Categorias añadidas',
        'clientes':str(count_clientes)+' Clientes añadidos',
        'status':200
    }
    '''  for i in Recursos:
        print (i.nombre_recurso)
    
    print('----------------------')
    for x in Categorias:
        print(x.nombre_categoria)
        for con in x.lista_configuraciones:
            print(con.id_config)    
            print(con.nombre_config)
            
            for rec in con.lista_recursos:
                print(rec['id_recurso'])
                print(rec['cantidad'])  
    print('----------------------')
    for z in Clientes:
        print(z.nombre_cliente) '''    

    #print(Dato)
    if configuracion != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})


#subir archivo de Consumos XML 
@app.route('/post-consumos', methods=['POST'])
def postConsumos():
    global Consumos
    
    #get xml info
    consumos = request.json['data']
    
    consum_files =  minidom.parseString(consumos)
    
    consumos = consum_files.getElementsByTagName('listadoConsumos')[0]
    consum_list = consumos.getElementsByTagName('consumo')
    count_consumos = 0
    for cns in consum_list:
        count_consumos += 1
        cliente_nit = cns.attributes['nitCliente'].value
        instance_id = cns.attributes['idInstancia'].value
        tiempo_consum = cns.getElementsByTagName('tiempo')[0]
        fechaHora = cns.getElementsByTagName('fechaHora')[0]
        new_consumo = Consumo(cliente_nit,instance_id,tiempo_consum.firstChild.data,fechaHora.firstChild.data)
        Consumos.append(new_consumo)
    
    Dato ={
        'data': 'archivo obtenido',
        'consumos':str(count_consumos)+' Consumos añadidos',
        'status':200
    }
    if consumos != '':
        response =jsonify(Dato)
        return(response)
    else:
        return jsonify({'data': 'error'})  


#------Operaciones del sistema----------------------------------------------------

#Obtener Categorias con sus configuraciones y lista de recursos
@app.route('/get-categorias', methods=['GET'])
def get_categorias():
    global Categorias
    list_categorias = []
    for c in Categorias:
        
        config =c.lista_configuraciones
        lista_configuraciones = []
        
        for conf in config:
            
            list_recu = conf.lista_recursos
            recursos_list = []
            for rec in list_recu:
                Dato_rec ={
                    'id_recurso':rec['id_recurso'],
                    'cantidad':rec['cantidad'],         
                }
                recursos_list.append(Dato_rec)
            
            Dato_conf ={
            'id':conf.id_config,
            'nombre':conf.nombre_config,
            'descripcion':conf.descripcion_config,
            'recursos': recursos_list,          
            }
            lista_configuraciones.append(Dato_conf)
        
        Dato ={
            'message':'get categorias',
            'id':c.id_categoria,
            'nombre':c.nombre_categoria,
            'descripcion':c.descripcion_categoria,
            'carga':c.carga_de_trabajo,
            'lista_conf': lista_configuraciones, 
        }
        
        list_categorias.append(Dato)
    respuesta = jsonify(list_categorias)
    return (respuesta)


#Obtener Clientes
@app.route('/get-clientes', methods=['GET'])
def get_clientes():
    global Clientes
    
    list_clientes = []
    
    for clt in Clientes:
        
        instancias = []
        
        for inst in clt.lista_Instancias:
            
            list_inst ={
                'id':inst.id_instance,
                'id_config':inst.id_configuracion,
                'nombre':inst.nombre_instance,
                'fecha_inicio':inst.fecha_inicio,
                'fecha_final':inst.fecha_final,
                'estado_instancia':inst.estado_instancia 
            }
            instancias.append(list_inst)
        
        Dato ={
            'status':200,
            'nit':clt.NIT,
            'nombre':clt.nombre_cliente,
            'user':clt.user,
            'password':clt.password,
            'direccion':clt.direccion,
            'email':clt.email,
            'lista_inst':instancias        
        }
        list_clientes.append(Dato)
    respuesta = jsonify(list_clientes)
    return (respuesta)


#obtener Recursos
@app.route('/get-recursos', methods=['GET'])
def get_recursos():
    global Recursos
    
    list_recursos = []
    
    for rec in Recursos:
        Dato={
            'id':rec.id_recurso,
            'nombre':rec.nombre_recurso,
            'abreviatura':rec.abreviatura_recurso,
            'metrica':rec.metrica,
            'tipo':rec.tipo,
            'costo':rec.costo
        }
        list_recursos.append(Dato)
    respuesta = jsonify(list_recursos)
    return (respuesta)


#obtener configuraciones
@app.route('/get-configuraciones', methods=['GET'])
def get_configs():
    global Configuraciones_glob
    
    list_configuraciones = []
    
    for conf in Configuraciones_glob:
        
        list_recu = conf.lista_recursos 
        recursos_list = []
        for rec in list_recu:
            Dato_rec ={
                'id_recurso':rec['id_recurso'],
                'cantidad':rec['cantidad'],         
            }
            recursos_list.append(Dato_rec)
            
        Dato_conf ={
        'id':conf.id_config,
        'nombre':conf.nombre_config,
        'descripcion':conf.descripcion_config,
        'recursos': recursos_list,          
        }
        list_configuraciones.append(Dato_conf)
            
    respuesta = jsonify(list_configuraciones)
    return (respuesta)


#Crear Configuracion django
@app.route('/crear-configuracion', methods=['POST'])
def createConfiguracion():
    global Configuraciones_glob
    
    configuracion = request.json['data']
    
    
    id = configuracion['id']
    nombre = configuracion['nombre']
    descripcion= configuracion['descripcion']
    recursos = configuracion['recursos']
    cantidad = configuracion['cantidad']
    
    recursos_list =[]
    
    Dato_rec ={
        'id_recurso':recursos,
        'cantidad':cantidad,
    }
    recursos_list.append(Dato_rec) 
    
    nuevaConfig = Configuracion(id,nombre,descripcion,recursos_list)
    Configuraciones_glob.append(nuevaConfig)
    
    Dato = {
                'message': 'Configuracion agregada Exitosamente',
                'state':200
            }
    respuesta = jsonify(Dato)
    return (respuesta)


#Crear Configuracion postman
@app.route('/crear-configuracion2', methods=['POST'])
def createConfiguracion2():
    global Configuraciones_glob
    
    configuracion = request.json['data']
    
    id = configuracion['id']
    nombre = configuracion['nombre']
    descripcion= configuracion['descripcion']
    recursos = configuracion['recursos']
    
    recursos_list =[]
    for rec in recursos:
        Dato_rec ={
            'id_recurso':rec['id_recurso'],
            'cantidad':rec['cantidad'],         
        }
        recursos_list.append(Dato_rec)           
    
    nuevaConfig = Configuracion(id,nombre,descripcion,recursos_list)
    Configuraciones_glob.append(nuevaConfig)
    
    Dato = {
                'message': 'Configuracion agregada Exitosamente',
                'state':200
            }
    respuesta = jsonify(Dato)
    return (respuesta) 


#Crear Recurso
@app.route('/crear-recurso', methods=['POST'])
def createRecurso():
    global Recursos
    
    
    recurso = request.json['data']
    
    id = recurso['id']
    nombre = recurso['nombre']
    abreviatura = recurso['abreviatura']
    metrica = recurso['metrica']
    tipo = recurso['tipo']
    costo = recurso['costo']
    
    nuevoRecurso = Recurso(id,nombre,abreviatura, metrica, tipo,costo)
    Recursos.append(nuevoRecurso)
    
    Dato = {
                'message': 'Recurso agregado Exitosamente',
                'state':200
            }
    respuesta = jsonify(Dato)
    return (respuesta)


#Crear Categoria postman
@app.route('/crear-categ', methods=['POST'])
def createCateg():
    global Categorias
    global Configuraciones_glob
    
    categoria = request.json['data']
    
    id = categoria['id']
    nombre = categoria['nombre']
    descripcion = categoria['descripcion']
    carga = categoria['carga']
    configuraciones = categoria['configuraciones']
    
    lista_conf = []
    
    for conf in configuraciones:
        for conf_g in Configuraciones_glob:
            if conf['id'] == conf_g.id_config:
                lista_conf.append(conf_g)
                break
    
    nuevaCateg = Categoria(id,nombre,descripcion, carga,lista_conf)
    Categorias.append(nuevaCateg)
    Dato = {
            'message': 'Categoria agregada Exitosamente',
            'state':200
            }
    respuesta = jsonify(Dato)
    return (respuesta)




if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port="5000")