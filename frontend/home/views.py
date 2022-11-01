from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom
from .forms import config_form, consume_form , crearRecurso_form ,crearConfig_form
from django.contrib import messages
import json
import requests

# Create your views here.
def consulta_page(request):
    return render(request, "consulta.html")

def carga_files(request):
    message =''
    if request.method == 'POST':
        if request.POST.get('config_file') != None:
            form = config_form(request.POST)
            if form.is_valid():
                data = request.POST.get('config_file')
                response= send_configFile(data)
                messg= response['categorias']+' '+response['clientes']+' '+response['recursos']
                print(response)
                message = messg
        else:
            form = consume_form(request.POST)
            if form.is_valid():
                data = request.POST.get('consumo_file')
                response= send_consumoFile(data)['consumos']
                message = response
    else:
        form = config_form()
       
    return render(request, "carga.html", {'form': form, 'message':message})

def send_configFile(data):
    request = requests.post('http://127.0.0.1:5000/post-config', json={'data': data})
    return json.loads(request.text)

def send_consumoFile(data):
    request = requests.post('http://127.0.0.1:5000/post-consumos', json={'data': data})
    return json.loads(request.text)

def consulta_Categorias(request):
    resp= requests.get('http://127.0.0.1:5000/get-categorias')
    
     #convert reponse data into json
    data = resp.json()
    return render(request, "view-catg.html",{'categorias': data})

def consulta_clientes(request):
   resp= requests.get('http://127.0.0.1:5000/get-clientes')
   data = resp.json()
   return render(request, "view-clientes.html",{'clientes': data})

def consulta_recursos(request):
    resp= requests.get('http://127.0.0.1:5000/get-recursos')
    data = resp.json()
    return render(request, "view-recursos.html",{'recursos': data})

def consulta_configuraciones(request):
    resp= requests.get('http://127.0.0.1:5000/get-configuraciones')
    data = resp.json()
    return render(request, "view-config.html",{'configuraciones': data})

def consulta_instancias(request):
    resp= requests.get('http://127.0.0.1:5000/get-instancias')
    data = resp.json()
    return render(request, "view-instances.html",{'instances': data})

def creacion_page(request):
    return render(request, "creacion_dash.html")

def crear_recurso(request):
    message =''
    if request.method == 'POST':
        form = crearRecurso_form(request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre_recurso')
            abreviatura = request.POST.get('abreviatura')
            tipo = request.POST.get('tipo')
            metrica = request.POST.get('metrica')
            costo = request.POST.get('costo')
            id = request.POST.get('id')
            
            dato ={
               'id':id,
               'nombre':nombre,
               'abreviatura':abreviatura,
               'metrica':metrica,
               'tipo':tipo,
               'costo':costo
            }
            response = sendCrear_recurso(dato)
            message = response['message']
            

    else:
        form = crearRecurso_form()    
    
    return render(request, "crear_recurso.html", {'form': form,'message':message})

def sendCrear_recurso(data):
    request = requests.post('http://127.0.0.1:5000/crear-recurso', json={'data': data})
    return json.loads(request.text)


def crear_config(request):
    message =''
    recursos = requests.get('http://127.0.0.1:5000/get-recursos')
    data = recursos.json()
    
    if request.method == 'POST':

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        id = request.POST['id']
        recursos = request.POST['recursos']
        cantidad = request.POST['cantidad']
        
        dato ={
           'id':id,
           'nombre':nombre,
           'descripcion':descripcion,
           'recursos':recursos,
           'cantidad':cantidad
        }
        response = sendCrear_config(dato)
        message = response['message']
        return render(request, "crear-config.html", {'message':message})    

    else:
        recursos = requests.get('http://127.0.0.1:5000/get-recursos')
        data = recursos.json()
        return render(request, "crear-config.html", {'message':message,'recursos':data})
    

def sendCrear_config(data):
    request = requests.post('http://127.0.0.1:5000/crear-configuracion', json={'data': data})
    return json.loads(request.text)

def crear_Categoria(request):
    message =''
    configuraciones = requests.get('http://127.0.0.1:5000/get-configuraciones')
    data = configuraciones.json()
    
    if request.method == 'POST':
        configuraciones =[]
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        id = request.POST['id']
        carga = request.POST['carga']
        for config  in data:
            if  config['id'] in request.POST:
                configuracion = request.POST[config['id']]
                id_config={
                    'id':configuracion
                }
                configuraciones.append(id_config)

        print(configuraciones)
        dato ={
           'id':id,
           'nombre':nombre,
           'descripcion':descripcion,
           'carga':carga,
           'configuraciones':configuraciones
        }
        print(dato)
        response = sendCrear_Categ(dato)
        message = response['message']
        return render(request, "crear-config.html", {'message':message})    

    else:
        configuraciones = requests.get('http://127.0.0.1:5000/get-configuraciones')
        data = configuraciones.json()
        return render(request, "crear-categ.html", {'message':message,'configuraciones':data})
    
def sendCrear_Categ(data):
    request = requests.post('http://127.0.0.1:5000/crear-categ', json={'data': data})
    return json.loads(request.text)

def crear_Cliente(request):
    message =''
    instancias = requests.get('http://127.0.0.1:5000/get-instancias')
    data = instancias.json()
    
    if request.method == 'POST':
        instancias_list =[]
        nit = request.POST['nit']
        nombre = request.POST['nombre']
        user = request.POST['user']
        password = request.POST['password']
        direccion = request.POST['direccion']
        email = request.POST['email']
        for inst  in data:
            if  inst['id'] in request.POST:
                instancia = request.POST[inst['id']]
                id_inst={
                    'id':instancia
                }
                instancias_list.append(id_inst)

        print(instancias_list)
        dato ={
           'nit':nit,
           'nombre':nombre,
           'user':user,
           'email':email,
           'password':password,
           'direccion':direccion,
           'instancias':instancias_list
        }
        print(dato)
        response = sendCrear_Cliente(dato)
        message = response['message']
        return render(request, "crear-cliente.html", {'message':message})    

    else:
        instancias = requests.get('http://127.0.0.1:5000/get-instancias')
        data = instancias.json()
        return render(request, "crear-cliente.html", {'message':message,'instancias':data})

def sendCrear_Cliente(data):
    request = requests.post('http://127.0.0.1:5000/crear-clientes', json={'data': data})
    return json.loads(request.text)


def crear_Instance(request):
    message =''
    configuraciones = requests.get('http://127.0.0.1:5000/get-configuraciones')
    data = configuraciones.json()
    
    if request.method == 'POST':
        nombre = request.POST['nombre_instance']
        id = request.POST['id']
        fecha = request.POST['fecha_inicial']
        configuracion = request.POST['configuracion']
        
        dato ={
           'id':id,
           'nombre':nombre,
           'fecha_inicio':fecha,
           'id_configuracion':configuracion
        }
        print(dato)
        response = sendCrear_instance(dato)
        message = response['message']
        return render(request, "crear-instance.html", {'message':message})    

    else:
        configuraciones = requests.get('http://127.0.0.1:5000/get-configuraciones')
        data = configuraciones.json()
        return render(request, "crear-instance.html", {'message':message,'configuraciones':data})
    
def sendCrear_instance(data):
    request = requests.post('http://127.0.0.1:5000/crear-instancia', json={'data': data})
    return json.loads(request.text)

def consultaFacturacion(request):
    message =''
    clientes = requests.get('http://127.0.0.1:5000/get-clientes')
    data = clientes.json()
    
    return render(request, "consulta-Fact.html",{'message':message,'clientes':data})

def buscar(request):
    if request.method == 'GET':
        nit = request.GET['id_cliente']
        dato ={
           'nit_cliente':nit
        }
        response = send_factura(dato)
        print(response)
    return render(request, "factura.html",{'factura':response})

def send_factura(data):
    request = requests.get('http://127.0.0.1:5000/gen-factura', json={'data': data})
    return json.loads(request.text)
