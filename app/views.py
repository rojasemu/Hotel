from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import CashRegister, Client, Room, Extra, Entry, Entry_extra, Room_Condition
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404





# Create your views here.

def index (request):
    
    return render (request,'index.html' )

#Registrar Cliente
def client (request):    
        
    if request.method =='POST':
            
        name= request.POST ['name'] 
        last_name = request.POST ['last_name']    
        document_type = request.POST ['document_type'] 
        document_number = request.POST ['document_number']    
        company = request.POST['company'] 
        phone = request.POST ['phone']    
        car = request.POST ['car'] 
        license_plate = request.POST ['license_plate']    
          
        
        client= Client.objects.create(
            name=name, last_name=last_name, document_type=document_type, 
            document_number=document_number, company=company, phone=phone,
            car=car, license_plate= license_plate
            )
        client.save()
        messages.success(request, 'Cliente Registrado')     
        return redirect('listclients')
    
    return render (request, 'client/gestionclientes.html', {
     
        
    })

#Editar cliente
def editclient(request, id):    
    client= Client.objects.get(id=id)    
   
    return render(request, "client/editarcliente.html",{
        
        'client':client
    })

#Editar cliente
def editc (request, id): 
        
    id = request.POST['cliente']
    name= request.POST ['name'] 
    last_name = request.POST ['last_name']    
    document_type = request.POST ['document_type'] 
    document_number = request.POST ['document_number']    
    company = request.POST['company'] 
    phone = request.POST ['phone']    
    car = request.POST ['car'] 
    license_plate = request.POST ['license_plate']            
    
    client = get_object_or_404(Client, pk=id)
    
    client.name =name        
    client.last_name= last_name 
    client.document_type=document_type
    client.document_number=document_number
    client.company=company
    client.phone=phone
    client.car=car
    client.license_plate=license_plate
    client.save()  
    
    return redirect ('listclients')
  

#Eliminar cliente       
def clientdelete (request,id):
        
    client = get_object_or_404(Client, pk=id)
    client.delete()
    #messages.success(request, 'Cliente Eliminado') 
    
    return redirect ('listclients')
  

#Listar clientes    
def list_client(request):
    
    queryset= request.GET.get("buscar")
    print(queryset)
    client=Client.objects.all()
    #messages.success(request, 'Clientes listados') 
    page =request.GET.get('page', 1)
    
    try:
        
        paginator = Paginator(client, 5)
        client =paginator.page(page)
    
    except:
        raise Http404
        
        
        
    if queryset:
        
        client=Client.objects.filter(            
            Q(name__icontains= queryset)|
            Q(document_number__iexact= queryset)
        ).distinct()                
               
    return render(request, 'client/gestionclientes.html',{
       
       'client':client, 
       'paginator':paginator              
     }                 
    
    )
     
     
 ##################################################    

#Listar Reservaciones   
def list_booking(request):
    
    queryset= request.GET.get("buscar")
    querysetr= request.GET.get("buscarr")
    print(queryset)
    
    #entry=Entry.objects.all()
    entry=Entry.objects.filter(type_entry='reservacion')             
    if queryset:        
       
        entry=Entry.objects.filter(            
        Q(entry_at__iexact= queryset, exit_at__iexact=querysetr)).distinct()
     
    page =request.GET.get('page', 1)    
    
    try:
        
        paginator = Paginator(entry, 2)
        entry =paginator.page(page)
    
    except:
        raise Http404     
             
        
               
    return render(request, 'booking/gestion_reservaciones.html',{
       
       'entry':entry,
       'paginator':paginator       
       #'client':client      
     }                 
    
    )    
 

#Editar Reservacion
def editbooking(request, id):    
    entry= Entry.objects.get(id=id)
    room =Room.objects.filter(condition='Habilitada')
    entry_extrapack=Entry_extra.objects.get(entry_id=id, extra_id=1)
    entry_extrain=Entry_extra.objects.get(entry_id=id, extra_id=2)
    entry_extraout=Entry_extra.objects.get(entry_id=id, extra_id=3)
    
    extra=Extra.objects.all() 
    for extras in extra:
        if extras.id == 1:
            extra_adic = extras.amount
        elif extras.id == 2:
            extra_check_in = extras.amount
        else:
            extra_check_out = extras.amount
    
    if request.method =='POST': 
          
        room_select = (request.POST['habitacion']).split(',')      
        
        type_entry= request.POST ['tipoingreso'] 
        type_reservation= request.POST ['tiporeservacion']         
        extra_adicional= request.POST.get('extra_adicional')           
        extra_in= request.POST.get('extra_in')           
        extra_out= request.POST.get('extra_out')                 
        quantity_adicional= request.POST['cantidad_adicional']       
        quantity_in= request.POST['cantidad_in']     
        quantity_out= request.POST['cantidad_out']        
        room= room_select[0]           
        entry_at= request.POST ['fechaentrada']    
        exit_at= request.POST ['fechasalida']    
        observation= request.POST ['observacion']      
        payment_type= request.POST ['tipopago']    
        received= request.POST ['dinerorecibido']      
        payment_details= request.POST ['detallepago']    
        customer_debt= request.POST ['deudacliente']      
        hotel_debt= request.POST ['deudahotel']      
        total= request.POST ['total']
                     
             
        Entry.objects.filter(id=id).update(
            type_entry=type_entry, type_reservation=type_reservation,
            room_id=room, entry_at=entry_at, exit_at=exit_at, observation=observation,
            payment_type=payment_type, payment_details=payment_details, received=received,
            customer_debt=customer_debt, hotel_debt=hotel_debt, total=total 
            )        
        if  extra_adicional == '1':
                quantity_adicional = quantity_adicional
        else :
            quantity_adicional = 0
            extra_adicional = 1
        
        if  extra_in == '2':
            quantity_in = quantity_in
        else :
            quantity_in = 0
            extra_in = 2
            
        if  extra_out == '3':
            quantity_out = quantity_out
        else :
            quantity_out = 0
            extra_out = 3
            
        Room.objects.filter(id=entry.room_id).update(condition='Reservada')     
        Room.objects.filter(id=room).update(condition='Reservada')       
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_adicional).update(quantity=quantity_adicional)    
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_in).update(quantity=quantity_in)    
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_out).update(quantity=quantity_out)       
        
        if type_entry == 'Reservacion':     
            
            Room.objects.filter(id=entry.room_id).update(condition='Reservada')
        
        else:
            Room.objects.filter(id=entry.room_id).update(condition='Habilitada')     
         
        return redirect ('reservaciones')  
        
   
    return render(request, "booking/editar_reservacion.html",{
        
        'entry':entry,
        'room':room,
        'entry_extrapack':entry_extrapack,
        'entry_extrain':entry_extrain,
        'entry_extraout':entry_extraout,
        'extra_adic' : extra_adic,
        'extra_check_in' : extra_check_in,
        'extra_check_out' : extra_check_out
        
    })

#Eliminar Reserva
def bookingdelete (request,id):
        
    entry= Entry.objects.get(pk=id)
    entry.delete() 
    Room.objects.filter(id=entry.room_id).update(condition='Disponible')
    
    return redirect ('reservaciones')
    

 ##################################################   





#Registrar hospedaje 
def registerguest (request, id):
    date = timezone.now()
    fechaentrada= request.GET.get("fechaentrada")
    fechasalida= request.GET.get("fechasalida")
    clients= Client.objects.get(id=id) 
    
   
    room =Room.objects.all()
    extra=Extra.objects.all()     
    entry= Entry.objects.all()
    
    
    for extras in extra:
        if extras.id == 1:
            extra_adic = extras.amount
        elif extras.id == 2:
            extra_check_in = extras.amount
        else:
            extra_check_out = extras.amount
    
       
    if request.method =='POST':
        
        room_select = (request.POST['habitacion']).split(',') 
        
        receptionist=request.POST ['recepcionista']  
        client= request.POST ['cliente'] 
        type_entry= request.POST ['tipoingreso'] 
        type_reservation= request.POST ['tiporeservacion']         
        extra_adicional= request.POST.get('extra_adicional')           
        extra_in= request.POST.get('extra_in')           
        extra_out= request.POST.get('extra_out')                 
        quantity_adicional= request.POST['cantidad_adicional']       
        quantity_in= request.POST['cantidad_in']     
        quantity_out= request.POST['cantidad_out']        
        room= room_select[0]           
        entry_at= request.POST ['fechaentrada']    
        exit_at= request.POST ['fechasalida']    
        observation= request.POST ['observacion']      
        payment_type= request.POST ['tipopago']    
        received= request.POST ['dinerorecibido']      
        payment_details= request.POST ['detallepago']    
        customer_debt= request.POST ['deudacliente']      
        hotel_debt= request.POST ['deudahotel']      
        total= request.POST ['total']     
            
        
        entry= Entry.objects.create(receptionist_id=receptionist, client_id=client, type_entry=type_entry, 
            type_reservation=type_reservation, room_id=room, entry_at=entry_at, exit_at=exit_at, observation=observation, payment_type=payment_type,
            received=received, payment_details=payment_details, customer_debt=customer_debt, hotel_debt=hotel_debt,
            total=total           
        )
        
        entry.save()
        
        if  extra_adicional == '1':
            quantity_adicional = quantity_adicional
        else :
            quantity_adicional = 0
            extra_adicional = 1
        
        if  extra_in == '2':
            quantity_in = quantity_in
        else :
            quantity_in = 0
            extra_in = 2
            
        if  extra_out == '3':
            quantity_out = quantity_out
        else :
            quantity_out = 0
            extra_out = 3
            
        extra_add_adicional=Entry_extra.objects.create(entry_id=entry.id , extra_id= extra_adicional, quantity=quantity_adicional)
        extra_add_adicional.save()
        extra_add_in=Entry_extra.objects.create(entry_id=entry.id , extra_id= extra_in, quantity=quantity_in)
        extra_add_in.save()
        extra_add_out=Entry_extra.objects.create(entry_id=entry.id , extra_id= extra_out, quantity=quantity_out)
        extra_add_out.save()              
       
        if type_entry == 'Reservacion':     
            
            roomc=Room_Condition.objects.create(room_id=entry.room_id, condition='Reservada', date =date)
            roomc.save()
            Room.objects.filter(id=entry.room_id).update(condition='Reservada') 
            
        elif type_entry == 'Hospedaje':
            roomc=Room_Condition.objects.create(room_id=entry.room_id, condition='Ocupada', date =date)
            roomc.save()
            Room.objects.filter(id=entry.room_id).update(condition='Ocupada') 
        
        return redirect ('listclients')
    
    return render (request, 'guest/register_guest.html', {
     
    'clients':clients,
    'room':room,
    'extra':extra,
    'entry':entry,
    'extra_adic' : extra_adic,
    'extra_check_in' : extra_check_in,
    'extra_check_out' : extra_check_out,
    'fechaentrada':fechaentrada,
    'fechasalida':fechasalida
 
    })
  

#Editar Hospedaje
def editguest(request, id):
    
        
    entry= Entry.objects.get(id=id)
    room =Room.objects.filter(condition='Habilitada')
    entry_extrapack=Entry_extra.objects.get(entry_id=id, extra_id=1)
    entry_extrain=Entry_extra.objects.get(entry_id=id, extra_id=2)
    entry_extraout=Entry_extra.objects.get(entry_id=id, extra_id=3)
    extra=Extra.objects.all() 
    
    for extras in extra:
        if extras.id == 1:
            extra_adic = extras.amount
        elif extras.id == 2:
            extra_check_in = extras.amount
        else:
            extra_check_out = extras.amount
    
    if request.method =='POST':        
        
        room_select = (request.POST['habitacion']).split(',') 
        
        type_entry= request.POST ['tipoingreso'] 
        type_reservation= request.POST ['tiporeservacion']         
        extra_adicional= request.POST.get('extra_adicional')           
        extra_in= request.POST.get('extra_in')           
        extra_out= request.POST.get('extra_out')                 
        quantity_adicional= request.POST['cantidad_adicional']       
        quantity_in= request.POST['cantidad_in']     
        quantity_out= request.POST['cantidad_out']        
        room= room_select[0]           
        entry_at= request.POST ['fechaentrada']    
        exit_at= request.POST ['fechasalida']    
        observation= request.POST ['observacion']      
        guest_exit= request.POST ['salida']      
        payment_type= request.POST ['tipopago']    
        received= request.POST ['dinerorecibido']      
        payment_details= request.POST ['detallepago']    
        customer_debt= request.POST ['deudacliente']      
        hotel_debt= request.POST ['deudahotel']      
        total= request.POST ['total']
                     
             
        Entry.objects.filter(id=id).update(
            type_entry=type_entry, type_reservation=type_reservation,
            room_id=room, entry_at=entry_at, exit_at=exit_at, observation=observation,guest_exit=guest_exit,
            payment_type=payment_type, payment_details=payment_details, received=received,
            customer_debt=customer_debt, hotel_debt=hotel_debt, total=total 
            )        
        if  extra_adicional == '1':
                quantity_adicional = quantity_adicional
        else :
            quantity_adicional = 0
            extra_adicional = 1
        
        if  extra_in == '2':
            quantity_in = quantity_in
        else :
            quantity_in = 0
            extra_in = 2
            
        if  extra_out == '3':
            quantity_out = quantity_out
        else :
            quantity_out = 0
            extra_out = 3
            
        Room.objects.filter(id=entry.room_id).update(condition='En Espera')         
        Room.objects.filter(id=room).update(condition='Ocupada')    
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_adicional).update(quantity=quantity_adicional)    
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_in).update(quantity=quantity_in)    
        Entry_extra.objects.filter(entry_id=id , extra_id= extra_out).update(quantity=quantity_out)       
         
        if guest_exit == 'Si':
            
            Room.objects.filter(id=entry.room_id).update(condition='En Espera') 
            
            
        return redirect ('hospedajes')  
        
   
    return render(request, "guest/editar_hospedaje.html",{
        
        'entry':entry,
        'room':room,
        'entry_extrapack':entry_extrapack,
        'entry_extrain':entry_extrain,
        'entry_extraout':entry_extraout,
        'extra_adic' : extra_adic,
        'extra_check_in' : extra_check_in,
        'extra_check_out' : extra_check_out
    })


#Listar Hospedajes   
def list_guest(request):
    
    queryset= request.GET.get("buscar")
    print(queryset)
    entry=Entry.objects.filter(type_entry='hospedaje')  
    queryset= request.GET.get("buscar")
    
    page =request.GET.get('page', 1)    
    
    try:
        
        paginator = Paginator(entry, 5)
        entry =paginator.page(page)
    
    except:
        raise Http404     
     
    if queryset:
        
        entry=Entry.objects.filter(            
            Q(room_id= queryset)).distinct()
            
                      
               
    return render(request, 'guest/gestion_hospedajes.html',{
       
       'entry':entry,
       'paginator':paginator       
               
     }                 
    
    )   
  
    
 ##################################################       

#Actualizar habitacion 
def edit_room(request, room_id):
    date = timezone.now()
    room= Room.objects.filter(id= room_id )
     
    if request.method =='POST':        
        
        condition= request.POST ['estado_habitacion']
        #date = request.POST['fecha']
        observation= request.POST ['observacion']   
        
        Room.objects.filter(id=room_id).update(condition=condition, observation= observation )    
        return redirect ('list_room')      
             
           
    return render(request, 'room/estadosroom.html',{
                
        'room': room,
        'date': date,   
              
        
    }        )
    
    
#listar todas la habitaciones
def list_Room(request): 
    p = 0
    date = timezone.now()
    queryset= request.GET.get("buscar")
        
    room= Room.objects.all()    
    roomh= Room.objects.filter( condition='habilitada').count()    
    roomd= Room.objects.filter( condition='Disponible').count()    
    roomo= Room.objects.filter( condition='Ocupada').count()    
    roomr= Room.objects.filter( condition='Reservada').count()    
    roome= Room.objects.filter( condition='En Espera').count()    
    rooma= Room.objects.filter( condition='Averiada').count()   
    #entry=Entry.objects.filter(Q( entry_at__lte = date) & Q( exit_at__gte = date))
    entry=Entry.objects.all()
    page =request.GET.get('page', 1)
    
    roomc=Room_Condition.objects.filter(date = date)
   
    
    try:
        
        paginator = Paginator(room, 30)
        room =paginator.page(page)
    
    except:
        raise Http404
    
    if queryset:        
       
        entry=Entry.objects.filter(Q( entry_at=queryset ) )   
        roomc=Room_Condition.objects.filter(Q( date=queryset ) )       
          
               
    return render(request, 'room/listroom.html',{
       
       'room':room,
       'roomh':roomh,
       'roomd':roomd,
       'roomo':roomo,
       'roomr':roomr,
       'roome':roome,
       'rooma':rooma,     
       'entry':entry,                    
       'paginator':paginator,
       'queryset':queryset,
       'date':date,
       'roomc':roomc,
       'p' : p, 
       
           
     }                
    )

#listar caja chica
def list_cashregister(request):
    
    cash=CashRegister.objects.all()

    return render(request, 'cashregister/caja.html',{
       
       'cash':cash,                     
     }                
    )



 ##################################################    
def login_page(request): 
       
     if request.user.is_authenticated:
         return redirect('index')
    
     else:             
        if request.method == 'POST':
        
            username = request.POST.get('username')
            password = request.POST.get('password')    
            user = authenticate(request, username=username, password=password)            
            if user is not None:         
                login(request, user)
                return redirect('/index')    
            
            else:
                messages.error(request,'Datos Incorrectos')       
    
    
        return render(request, 'login.html',{
            
           'User':User
            
        })
    
    
def logout_user (request):
        
    logout(request)
    
    return redirect('login')