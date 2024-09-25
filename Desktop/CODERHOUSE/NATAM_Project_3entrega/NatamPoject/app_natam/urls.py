

from django.urls import path
from .views import (nuevo_login,
    nuevo_register,
    nuevo_ticket,inicio,
    login2, 
    register,
    ticket,
    login_formulario,
    busqueda_usuario_formulario,
    busqueda_usuario_resultado,
    register_formulario,
    ticket_formulario
)

urlpatterns = [
  
  
    
    path('inicio/', inicio,name="inicio"),
    path('login/', login2,name="login"),
    path('register/', register,name="register"),
    path('ticket/', ticket,name="ticket"),
    path('login-formulario/',login_formulario,name="loginFormulario"),
    path('register-formulario',register_formulario,name="registerFormulario"),
    path('ticket-formulario',ticket_formulario,name="ticketFormulario"),
    path('Bien/',login_formulario,name="bien"),
    path('busqueda-usuario/',busqueda_usuario_formulario, name="busquedaUsuario"),
    path('busquedaUsuarioResultado/',busqueda_usuario_resultado,name="busquedaUsuarioResultado"),


#1:27
   
]
