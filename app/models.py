
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from app.choice import Tipo_Documento, Tipo_habitacion, Estado_habitacion, Tipos_Pagos,Estatus
from django.utils import timezone

# Create your models here.



class Company(models.Model):
    
    name=models.CharField(max_length=80, verbose_name='Nombre')
    mail=models.EmailField(max_length=250, verbose_name='Correo')
    address=models.CharField(max_length=250, verbose_name='Direccion')
    phone=models.CharField(max_length=20, verbose_name='Numero de Telefono')
    rif= models.CharField(max_length=40, verbose_name='Rif')


    class Meta:
            
            verbose_name ='Empresa'
            verbose_name_plural ='Empresas'  
            
            
            
            

class CashRegister(models.Model):
    
    balance_in=models.FloatField( verbose_name='Saldo Entrada')
    balance_out=models.FloatField( verbose_name='Saldo Salida')
    observation=models.TextField(verbose_name='Observaciones', null=True, blank=True)
    date=models.DateField(verbose_name='Fecha')
    receptionist=models.ForeignKey(User, on_delete=models.CASCADE) 


    class Meta:
            
            verbose_name ='Caja Chica'
            #verbose_name_plural ='Cajas Chicas'  




 
class Client(models.Model):
    
    name = models.CharField (max_length=60, verbose_name='Nombre')     
    last_name = models.CharField(max_length=60, verbose_name='Apellidos')      
    document_type = models.CharField(max_length=20, choices=Tipo_Documento, default='Cedula',  verbose_name='Tipo de documento')
    document_number =models.IntegerField(verbose_name='Numero De Documento')
    company =models.CharField(max_length= 80, null=True, blank=True, verbose_name='empresa')
    phone=models.CharField(max_length=20, verbose_name='Numero de telefono')
    car=models.CharField(max_length=30,null=True, blank=True, verbose_name='vehiculo')
    license_plate=models.CharField(max_length=10,null=True, blank=True, verbose_name='Placa Vehiculo')   
       
    class Meta:
        
        verbose_name ='Cliente'
        verbose_name_plural ='Clientes'        
        
    def __str__(self):
        return self.name
    
     
    
class Employee(models.Model): 
    
    names=models.CharField(max_length=60, verbose_name='Nombre')
    identification_card=models.IntegerField(verbose_name='Numero de Cedula')    
    occupation=models.CharField(max_length=60, verbose_name='Ocupacion')  
    
    
    
    class Meta:
            
            verbose_name ='Empleado'
            verbose_name_plural ='Empleados'  







class Extra(models.Model):
    
    name =models.CharField(max_length=100, verbose_name='Extra')
    description=models.TextField(verbose_name='Descripcion')
    amount=models.FloatField(verbose_name='Monto Extra')    


    class Meta:
            
            verbose_name ='Extra'
            verbose_name_plural ='Extras'  





        
class Room(models.Model):
    
    room_number=models.CharField(max_length=3, verbose_name='Numero de Habitacion')
    room_type=models.CharField(max_length=40, choices=Tipo_habitacion, default='Estandar', verbose_name='Tipo de Habitacion')
    condition=models.CharField(max_length=20, choices=Estado_habitacion, default='Habilitada', verbose_name='Estado de la Habitacion')
    observation=models.TextField(verbose_name='Observaciones')  
    room_price=models.FloatField(verbose_name='Precio de Habitacion')
     
    class Meta:
        
        verbose_name ='Habitacion'
        verbose_name_plural ='Habitaciones'
        
        
    def __str__(self):
        
        return self.room_number
    
    
    
    
class Room_Condition(models.Model):
    
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    condition=models.CharField(max_length=20, choices=Estado_habitacion, default='Habilitada', verbose_name='Estado de la Habitacion', null=True)
    date=models.DateField(verbose_name='Fecha')
    
    class Meta:
        
        verbose_name ='Habitacion Condicion'       
        
        
    def __str__(self):        
        
        return self.condition
    
    
    
    
    
class Entry (models.Model):
    
    client=models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cliente")
    extra=models.ManyToManyField(Extra, through='Entry_extra')    
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    receptionist=models.ForeignKey(User, on_delete=models.CASCADE)
    type_entry=models.CharField(max_length=50, verbose_name='Tipo de Ingreso')
    type_reservation=models.CharField(max_length=50, default='No Cancelada', verbose_name='Tipo de Reservacion')
    observation=models.TextField(null=True, blank=True, verbose_name='Observacion')
    payment_type=models.CharField( max_length=20, choices=Tipos_Pagos, default='Efectivo', verbose_name='Tipo de Pago')
    payment_details=models.CharField(max_length=250, verbose_name='Detalles del Pago')
    total=models.FloatField(verbose_name='Total', null=True )
    customer_debt=models.FloatField(verbose_name='Deuda Cliente', null=True, blank=True)
    hotel_debt=models.FloatField(verbose_name='Deuda Hotel', null=True, blank=True)
    received=models.FloatField(verbose_name='Dinero Recibido')
    entry_at=models.DateField(verbose_name='Entrada el')
    exit_at=models.DateField(verbose_name='Salida el', null=True, blank=True)
    guest_exit=models.CharField(max_length=2, default="No", verbose_name="salida", null=True )
   
    
    class Meta:
            
            verbose_name ='Huesped'
            verbose_name_plural ='Huespedes'  
    


class Entry_extra(models.Model):

    extra=models.ForeignKey(Extra, on_delete=models.CASCADE)
    entry=models.ForeignKey(Entry, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)



''' class Booking (models.Model):
    
    room=models.ForeignKey(Room, on_delete=models.CASCADE)   
    reservation=models.CharField(max_length=50, verbose_name='Tipo de Reservacion')
    entry_at=models.DateField(verbose_name='Fecha de Ingreso')    
    entry_at=models.DateField(verbose_name='Fecha de Salida')    
    observation=models.TextField(null=True, blank=True, verbose_name='Observacion')
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    receptionist=models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    class Meta:
        
        verbose_name ='Reservacion'
        verbose_name_plural ='Reservaciones'
        ordering = ['-entry_at'] '''




class Breakdown(models.Model):
    
    
    guest=models.ForeignKey(Entry, null=True,on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)    
    report_date=models.DateField(verbose_name='Reportado el')
    observation=models.TextField(verbose_name='Observaciones', null=True, blank=True)  
    description_fails=models.TextField(verbose_name='Observaciones', null=True, blank=True)
    start_repair=models.DateField(verbose_name='Inicio de Reparacion el')
    end_repair=models.DateField(verbose_name='Fin de Reparacion el', null=True)
    status=models.CharField( max_length=20, choices=Estatus, default='Atendida', verbose_name='Estatus')


    class Meta:
            
        verbose_name ='Averia'
        verbose_name_plural ='Averias'  
    
    
    


class Ropen(models.Model):

    receptionist=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Recepcionista Abre Reporte')
    failure =models.ForeignKey(Breakdown, on_delete=models.CASCADE, verbose_name= 'Falla')


    class Meta:
            
        verbose_name ='Reporte Abierto'
        verbose_name_plural ='Reportes Abiertos'  




class Rclose(models.Model):

    receptionist=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Recepcionista Cierre Falla')
    failure =models.ForeignKey(Breakdown, on_delete=models.CASCADE, verbose_name= 'Falla')
    
    
    class Meta:
            
            verbose_name ='Reporte Cerrado'
            verbose_name_plural ='Reportes Cerrados'  


    
    

class Remployee(models.Model):
    
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name= 'Empleado')
    failure =models.ForeignKey(Breakdown, on_delete=models.CASCADE, verbose_name= 'Falla')
    
    
    
    class Meta:
            
            verbose_name ='Reporte Empleado'
            verbose_name_plural ='Reportes Empleados'  

    
    
    


class Memployee(models.Model):
    
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name= 'Empleado Mtto')
    failure =models.ForeignKey(Breakdown, on_delete=models.CASCADE, verbose_name= 'Falla')
    
    class Meta:
            
            verbose_name ='Personal Mantenimiento'
            verbose_name_plural ='Personal Mantenimientos'  
