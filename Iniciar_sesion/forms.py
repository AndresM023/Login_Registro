from django import forms
from django.forms import ModelForm
from Iniciar_sesion.models import Login_Regist

class Registro(ModelForm):
    class Meta:
        model = Login_Regist
        fields = ['usuario','correo_electronico','clave','clave2']
        widgets = {
            'usuario': forms.TextInput(attrs={'id':'user','type':'text','required':False}),
            'correo_electronico': forms.EmailInput(attrs={'id':'correo','type':'text','required':False}),
            'clave': forms.PasswordInput(attrs={'type':'password','id':'contraseña','required':False}),
            'clave2': forms.PasswordInput(attrs={'type':'password','id':'contra2','required':False}),
        }

# class Logeo(ModelForm):
#     class Meta:
#         model = Login
#         fields = '__all__'
#         widgets = {
#             'correo_elec': forms.EmailInput(attrs={'id': 'correo1', 'type': 'text', 'required': False}),
#             'clave3': forms.PasswordInput(attrs={'type': 'password', 'id': 'contraseña1', 'required': False})
#         }
#
