from django.db import models


class Login_Regist(models.Model):
    usuario = models.CharField(max_length=20, unique = True, default=None)
    correo_electronico = models.EmailField(max_length=100,unique=True)
    clave = models.CharField(max_length=100,default=None)
    clave2 = models.CharField(max_length=100, default=None)
    codigo = models.CharField(max_length=6)



# class Login(models.Model):
#     correo_elec = models.EmailField(max_length=100)
#     clave3 = models.CharField(max_length=100,default=None)
#
