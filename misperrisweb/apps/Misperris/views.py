from django.shortcuts import render
from .models import perro,sexo,usuario,comuna,region,tipoVivienda,tipoUsuario,estado,raza,adopcion
import sys
from itertools import cycle
import datetime
import smtplib
import shutil, os
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import time




# Create your views here.
def index(request):
    pe=perro.objects.all()
    
    if  request.user.is_authenticated:
        na=request.user.is_staff
        if na ==True:
            return render(request,'index.html',{'perritos':pe,'ingresado':True,'na':na,'admin':True})
        else:
            return render(request,'index.html',{'perritos':pe,'ingresado':True,'na':na})
        

    else:
        return render(request,'index.html',{'perritos':pe,'deslog':True})
@login_required
def logout(request):
    pe=perro.objects.all()
    auth.logout(request)
    return render(request,'index.html',{'perritos':pe,'deslog':True})


    


@login_required
def perros(request):
    pe=perro.objects.all()
    estad=estado.objects.all()
    username=request.user.username
    if request.POST:
        accion=request.POST.get("btnAccion")
        if accion == "Filtrar":
            se=request.POST.get("cboSelec")
            if se=="0":
                se=3
            pe=perro.objects.filter(idEstado=se)
           
            return render(request,'PerrosDis.html',{'perrito':pe,'estados':estad,'s':True})
           
                
        else:
            if accion == "Ver":
                ids=request.POST.get("oculto");       
                perri=perro.objects.get(name=ids)
                return render(request,'PerfilPerro.html',{'perri':perri})
            else:
                ids=int(request.POST.get("oculto2"))
            
                perris=perro.objects.get(name=ids)
                ds=estado.objects.get(name=3)
                
                perris.idEstado=ds
                adopc=adopcion.objects.all()
                i=1
                                
                for o in adopc:
                    i=i+1
                usernames=usuario.objects.get(usuario=username)
                adopci =adopcion(
                    name=i,
                    fecha=time.strftime("%x"),
                    IdPerro=perris,
                    idUsuario=usernames
                )
                perris.save()
                usernames.save()
                adopci.save()
                return render(request,'PerfilPerro.html',{'perri':perris,'adoptado':True})
                
            
        
        
    else:
        return render(request,'PerrosDis.html',{'perrito':pe,'estados':estad})

    

def login(request):
    usus=usuario.objects.all()
    pe=perro.objects.all()
    
    if request.POST:

        user=request.POST.get("txtEmail","")
        passa=request.POST.get("txtPass","")
        user=auth.authenticate(username=user,password=passa)
        if user is not None and user.is_active:
            auth.login(request,user)
            na=request.user.is_staff
            if na == True :
                pe=perro.objects.all()
                return render(request,'index.html',{'ingresado':True,'pe':pe,'admin':True})
            else:
                pe=perro.objects.all()
                return render(request,'index.html',{'ingresado':True,'pe':pe})
            
        else:
            return render(request,'login.html',{'error':True})
        

    else:
        return render(request,'login.html')
        
       
@login_required
def agregarperros(request):
    estad=estado.objects.all()
    raz=raza.objects.all()
    perros=perro.objects.all()
    if request.POST:
        nombrep=request.POST.get("txtNombrePerro")
        descriperro=request.POST.get("txtDescripcion")
        razs=request.POST.get("cboRaza")
        estadi=request.POST.get("cboEstado")
        imagen=request.FILES.get("imagen")
        estados=estado.objects.get(name=estadi)
        razas=raza.objects.get(name=razs)
        i=1
        for s in perros:
            i=i+1
        i=i+1
        perr =perro(
            name=i,
            descripcion=descriperro,
            nombrePerro=nombrep,
            idEstado=estados,
            idRaza=razas,
            imagenPerro=imagen        
        )
        perr.save()
        return render(request,'agregarPerros.html',{'est':estad,'raza':raz,'conf':True})
            


        
    else:
        na=request.user.is_staff
        if na == True:
            return render(request,'agregarPerros.html',{'est':estad,'raza':raz})
        else:
            pe=perro.objects.all()
            return render(request,'index.html',{'ingresado':True,'pe':pe})

@login_required
def registroAdmin(request):
    comun=comuna.objects.all()
    regi=region.objects.all()
    viv=tipoVivienda.objects.all()
    sexos=sexo.objects.all()
    tipos=tipoUsuario.objects.all()

    if request.POST:
        nombre=request.POST.get("txtNombre")
        usuarioname=request.POST.get("txtUsuario")
        passa=request.POST.get("txtPass")
        passa2=request.POST.get("txtPassconf")
        fnaci=request.POST.get("fecha")
        regions=request.POST.get("cboRegion")
        comunas=request.POST.get("cboComuna")
        telefono=request.POST.get("txtTelefono")
        idtvivienda=request.POST.get("cboTipoVivienda")
        idSexo=request.POST.get("cboSexo")
        rut=request.POST.get("txtRut") 
        correo=request.POST.get("txtCorreo")
        tipouser=request.POST.get("tipoUsuario")
        anio=int(fnaci[:4])
        actual= datetime.date.today()
        actual=actual.year
        tipoViviendac=tipoVivienda.objects.get(name=idtvivienda)
        sexoc=sexo.objects.get(name=idSexo)
        tipouserc=tipoUsuario.objects.get(name=tipouser)
        regionc=region.objects.get(name=regions)
        comunac=comuna.objects.get(name=comunas)
        usus=usuario.objects.all()
        i=0
        for u in usus:

            i=i+1
        i=i+2


        
        if passa == passa2:
            if validarRut(rut) == True:
                if actual-anio >17:
                    if verificar(usuarioname) ==True:
                        usuar =usuario(


                            name=i,

                            usuario=usuarioname,

                            rut=rut,

                            correo=correo,

                            passa=passa,

                            idRegion=regionc,

                            idComuna=comunac,

                            idTipoVivienda=tipoViviendac,

                            idSexo=sexoc,

                            idTipoUsuario=tipouserc



                            )
                            
                        user = User.objects.create_user(usuarioname, correo, passa)

                        usuar.save() 
                        if tipouser == "2":
                            user.is_staff = True
                        user.save()

                        return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'conf':True})
                        
                    else:
                        return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'existente':True})
                else:
                    return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'edin':True})

                                  

            
            else:
                return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'rutin':True})
                
        else:
            return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'passin':True})
    else:
        na=request.user.is_staff
        if na == True:
            return render(request,'registroAdmin.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos})
        else:
            pe=perro.objects.all()
            return render(request,'index.html',{'ingresado':True,'perritos':pe})
        

    

    
def validarRut(rut):

	rut = rut.upper()

	rut = rut.replace("-","")

	rut = rut.replace(".","")

	aux = rut[:-1]

	dv = rut[-1:]

 

	revertido = map(int, reversed(str(aux)))

	factors = cycle(range(2,8))

	s = sum(d * f for d, f in zip(revertido,factors))

	res = (-s)%11

 

	if str(res) == dv:

		return True

	elif dv=="K" and res==10:

		return True

	else:

		return False

 
def verificar(usuar):
    usuarios=usuario.objects.all()
    for us in usuarios:
        if us.usuario == usuar:
            return False
    return True

    
 
            

            

def registro(request):
    comun=comuna.objects.all()
    regi=region.objects.all()
    viv=tipoVivienda.objects.all()
    sexos=sexo.objects.all()
    tipos=tipoUsuario.objects.all()

    if request.POST:
        nombre=request.POST.get("txtNombre")
        usuarioname=request.POST.get("txtUsuario")
        passa=request.POST.get("txtPass")
        passa2=request.POST.get("txtPassconf")
        fnaci=request.POST.get("fecha")
        regions=request.POST.get("cboRegion")
        comunas=request.POST.get("cboComuna")
        telefono=request.POST.get("txtTelefono")
        idtvivienda=request.POST.get("cboTipoVivienda")
        idSexo=request.POST.get("cboSexo")
        rut=request.POST.get("txtRut") 
        correo=request.POST.get("txtCorreo")
        anio=int(fnaci[:4])
        actual= datetime.date.today()
        actual=actual.year
        tipoViviendac=tipoVivienda.objects.get(name=idtvivienda)
        sexoc=sexo.objects.get(name=idSexo)
        tipouserc=tipoUsuario.objects.get(name=1)
        regionc=region.objects.get(name=regions)
        comunac=comuna.objects.get(name=comunas)
        usus=usuario.objects.all()
        i=0
        for u in usus:

            i=i+1
        i=i+1


        
        if passa == passa2:
            if validarRut(rut) == True:
                if actual-anio >17:
                    if verificar(usuarioname) ==True:
                        usuar =usuario(


                            name=i,

                            usuario=usuarioname,

                            rut=rut,

                            correo=correo,

                            passa=passa,

                            idRegion=regionc,

                            idComuna=comunac,

                            idTipoVivienda=tipoViviendac,

                            idSexo=sexoc,

                            idTipoUsuario=tipouserc



                            )
                            
                        user = User.objects.create_user(usuarioname, correo, passa)

                        usuar.save() 
                        user.save()

                        return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'conf':True})
                        
                    else:
                        return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'existente':True})
                else:
                    return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'edin':True})

                                  

            
            else:
                return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'rutin':True})
                
        else:
            return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos,'passin':True})
    else:
        return render(request,'registro.html',{'comu':comun,'regiones':regi,'vivi':viv,'sex':sexos,'tipos':tipos})

    
                
def recuperar(request):

    if request.POST:
        usuarion=request.POST.get("txtUsuario")
        try:

            user=usuario.objects.get(usuario=usuarion)
        except Exception as ex:
            return render(request,'recuperar.html',{'noexiste':True})
        us=user.usuario
        passa=user.passa
        email=user.correo
        
        
        ms='Hola '+us+' gracias pos usar nuestro sistema de recuperacion de usuario su clave es '+passa
        
        fromaddr = 'misperris5@gmail.com'
        toaddrs  = email
        msg = ms
        username = 'misperris5@gmail.com'
        password = 'misperris1998'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs,msg)
        server.quit()

        return render(request,'recuperar.html',{'correo':email})
    else:
        return render(request,'recuperar.html')



@login_required
def administrar(request):
    na=request.user.is_staff
    per=perro.objects.all()    
    if na == True:
        if request.POST:
            hola=request.POST.get("btnEliminar")
            return render(request,'administrar.html',{'perros':per,'h':hola,'admin':True})

        else:
            return render(request,'administrar.html',{'perros':per,'admin':True})
        
    else:
        return render(request,'index.html',{'ingresado':True,'perritos':per})

@login_required    
def eliminar(request):
    na=request.user.is_staff
    per=perro.objects.all()
    if na == True:
        if request.POST:
            idd=request.POST.get("cboPerros")

            if idd != "0":
                pe=perro.objects.get(name=idd)
                pe.delete()
                return render(request,'eliminar.html',{'perros':per,'eliminado':True,'admin':True})

            else:
                return render(request,'eliminar.html',{'perros':per,'admin':True})
                
           
        else:
            return render(request,'eliminar.html',{'perros':per,'admin':True})
    else:
        return render(request,'index.html',{'ingresado':True,'perritos':per})

@login_required
def modificar(request):
    per=perro.objects.all()
    na=request.user.is_staff
    raz=raza.objects.all()
    est=estado.objects.all()
    
    if na == True:
        accion=request.POST.get("btnAccion")
        if request.POST:
            select=request.POST.get("cboPerros")
            if accion == "Buscar":
                

                if select!="0":
                    pere=perro.objects.get(name=select)
                    return render(request,'modificar.html',{'perros':per,'p':pere,'raz':raz,'est':est})
                else:
                    return render(request,'modificar.html',{'perros':per,'error':True,'raz':raz,'est':est})
            else:
                if select!="0":         
                    pere=perro.objects.get(name=select)
                    ndescripcion=request.POST.get("txtDescripcion")
                    iraza=request.POST.get("cboRaza")
                    iestado=request.POST.get("cboEstado") 
                    nestado=estado.objects.get(name=iestado)
                    nraza=raza.objects.get(name=iraza)
                    pere.descripcion=ndescripcion
                    pere.idRaza=nraza
                    pere.idEstado=nestado
                    pere.save()
                    return render(request,'modificar.html',{'perros':per,'error':True,'raz':raz,'est':est,'correcto':True})
                else:
                    return render(request,'modificar.html',{'perros':per,'error':True,'raz':raz,'est':est})
                
            
        else:
            return render(request,'modificar.html',{'perros':per,'error':True,'raz':raz,'est':est})
                
    else:
        return render(request,'index.html',{'ingresado':True,'perritos':per})
@login_required
def adopciones(request):
    adopciones=adopcion.objects.all()
    if request.user.is_staff == True:
        return render(request,'adopciones.html',{'adop':adopciones})
    else:
        per=perro.objects.all()
        return render(request,'index.html',{'ingresado':True,'perritos':per})