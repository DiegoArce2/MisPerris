from django.db import models

class region(models.Model):

    name=models.IntegerField(primary_key=True,verbose_name="idRegion") #name: solo primaria(siempre)

    descripcion=models.CharField(verbose_name="descripcion",max_length=30) #revisar en caso de terremoto en el codigo

    def __str__(self):

        return self.descripcion

class comuna(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idComuna")
    descripcion=models.CharField(verbose_name="descripcion",max_length=30)
    idRegion=models.ForeignKey(region,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

class tipoUsuario(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idTipoUsuario")
    descripcion=models.CharField(verbose_name="descripcion",max_length=30)
    def __str__(self):

        return self.descripcion

class tipoVivienda(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idTipoVivienda")
    descripcion=models.CharField(verbose_name="descripcion",max_length=30)

    def __str__(self):
        return self.descripcion

class sexo(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idSexo")
    descripcion=models.CharField(verbose_name="descripcion",max_length=30)
    def __str__(self):
        return self.descripcion
        



class usuario(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idUsuario")
    usuario=models.CharField(verbose_name="user",max_length=30)
    rut=models.CharField(verbose_name="rut",max_length=30,default='rut')
    correo=models.CharField(verbose_name="correo",max_length=30,default='correo')
    passa=models.CharField(verbose_name="passa",max_length=20,default='pass')
    idRegion=models.ForeignKey(region,on_delete=models.CASCADE)
    idComuna=models.ForeignKey(comuna,on_delete=models.CASCADE)
    idTipoVivienda=models.ForeignKey(tipoVivienda,on_delete=models.CASCADE)
    idSexo=models.ForeignKey(sexo,on_delete=models.CASCADE)
    idTipoUsuario=models.ForeignKey(tipoUsuario,on_delete=models.CASCADE,default='1')
    def __str__(self):
        return self.usuario

class raza(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idRaza")
    descripcion=models.CharField(verbose_name="descripcion",max_length=20)   
    def __str__(self):
        return self.descripcion

class estado(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idEstado")
    descripcion=models.CharField(verbose_name="descripcion",max_length=20) 
    def __str__(self):
        return self.descripcion


#terminar
class perro(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idPerro")
    descripcion=models.CharField(verbose_name="descripcion",max_length=30)
    nombrePerro=models.CharField(max_length=30,default='nn')
    idEstado=models.ForeignKey(estado,on_delete=models.CASCADE)
    idRaza=models.ForeignKey(raza,on_delete=models.CASCADE)
    imagenPerro=models.FileField(upload_to='perros/')

    def __str__(self):
        return self.nombrePerro

    
class adopcion(models.Model):
    name=models.IntegerField(primary_key=True,verbose_name="idAdopcion")
    fecha=models.CharField(verbose_name="fecha",max_length=20)
    IdPerro=models.ForeignKey(perro,on_delete=models.CASCADE)
    idUsuario=models.ForeignKey(usuario,on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha