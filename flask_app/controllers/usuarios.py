from flask_app import app
from flask import render_template, request, redirect, flash
from flask_app.models.usuario import Usuario


@app.route('/')
def inicio(): 
    return render_template('index.html')

#registro / crear usuario
@app.route('/crear_usuario', methods= ["POST"])
def crear_usuario():

    #para agregar un usuario lo primero que debo hacer es
    #recuperar la informacion desde el formulario
    #para hacer eso necesitamos el request.form
    #%(nombre)s, %(apellido)s, %(email)s,%(password)s

    #--- IMPORTANTE: TEORICAMENTE ANTES DE REGISTRAR UN NUEVO DATO
    #--- YO DEBERÍA VALIDAR QUE LOS DATOS INGRESADOS
    #--- SEAN VALIDOS

    if not Usuario.validar_usuario(request.form):
        
        return redirect('/')

    #--- VALIDACIONES ---

    datos_usuario_registro= {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
         'password':request.form['password']
    }
    
    return ''

#inicio sesión 


#cerrar sesión
