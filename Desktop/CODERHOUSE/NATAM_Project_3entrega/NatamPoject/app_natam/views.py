from django.shortcuts import redirect
from django.shortcuts import render
from. models import login,register,Ticket

from django .http import HttpResponse
# Create your views here.

def nuevo_login(req,username, password ):

    nuevo_login = login(username=username ,password =password)
    nuevo_login.save()

    return HttpResponse("""<p> Login:{nuevo_login.username} - Password {nuevo_login.password} creado con exito </p> 
    """)

def nuevo_register(req,name,lastName,rut,email,phone,birth_day):

        nuevo_register = register (name=name,lastName =lastName,rut=rut,email=email,phone=phone,birth_day=birth_day)
        nuevo_register.save()
        
        return HttpResponse("""<p> Registro:{nuevo_register.name} -  {nuevo_register.lastName}- {nuevo_register.rut} - {nuevo_register.email} - {nuevo_register.phone}- {nuevo_register.birth_day} creado con exito </p> 
        """)



def nuevo_ticket(req,flight_number,name_passenger,lastName_passenger,fligt_date, fligh_time,gate, origin, destination):

        nuevo_ticket = Ticket (
               flight_number=flight_number,
               name_passenger=name_passenger,
               lastName_passenger=lastName_passenger,
               fligt_date=fligt_date,
               fligh_time=fligh_time,
               gate=gate,
               origin=origin,
               destination=destination
            )
        nuevo_ticket.save()
        
        return HttpResponse("""<p> Ticket:{nuevo_ticket.flight_number} -  {nuevo_register.name_passenger}- {nuevo_register.lastName_passenger} - {nuevo_ticket.fligt_date} - {nuevo_ticket.fligh_time}- 
                            {nuevo_ticket.gate}-{nuevo_ticket.origin}-{nuevo_ticket.destination} creado con exito </p> 
        """)

def inicio (req):
       return render (req,"inicio.html")


def login2 (req):
       return render (req,"login.html ")
       


def ticket(req):
        return render (req, "ticket.html")


def bien(req):
        return render (req, "bien.html")



def login_formulario(req):
    print (req.POST)
       
    if req.method =='POST':
        nuevo_login = login(username=req.POST["username"], password=req.POST["password"])
        nuevo_login.save()

        return render(req,"bien.html",{})
    else:

       return render (req,"login_formulario.html",{})
    

def busqueda_usuario_formulario(req):
      return render (req,"busqueda_usuario.html")


# def busqueda_usuario_resultado (req):
#       return HttpResponse (f'Buscando usuario {req.GET["usuario"]}')




def busqueda_usuario_resultado(req):

    username = req.GET.get("usuario")

    username = login.objects.filter (username=username)

    if username:
      
        return render(req,"Usuario_Encontrado.html",{"Username":username})
    else:

        return render(req, "Usuario_NoEncontrado.html")
    

    
def register_formulario(req):
    print (req.POST)
       
    if req.method =='POST':
            nuevo_register = register (name=req.POST["name"],  
            lastName =req.POST["lastName"],
            rut =req.POST["rut"],
            email =req.POST["email"],
            phone =req.POST["phone"],
            birth_day =req.POST["birth_day"])

            nuevo_register.save()

            return render(req,"bien.html",{})
    else:

            return render (req,"register_formulario.html",{})
    

def ticket_formulario(req):
    print (req.POST)
       
    if req.method =='POST':
        nuevo_ticket = Ticket (flight_number =req.POST["flight_number"], 
        name_passenger=req.POST["name_passenger"],
        lastName_passenger=req.POST["lastName_passenger"],
        fligt_date =req.POST["flight_date"],
        fligh_time=req.POST["flight_time"],
        gate=req.POST["gate"],
        origin=req.POST["origin"],
        destination=req.POST["destination"])


        nuevo_ticket.save()

        return render(req,"bien.html",{})
    else:

         return render (req,"ticket_formulario.html",{})
    









