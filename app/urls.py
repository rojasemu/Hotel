from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

urlpatterns = [
    path('',views.login_page, name="login"),
        
    path('index', views.index, name="index"),
    
    path('logout',views.logout_user, name="logout"),
    
    path('habitaciones/',views.list_Room, name='list_room'),    
    #path('habitaciones/<int:id>',views.list_Room, name='list_room'),    
    path('Actualizar-habitacion/<int:room_id>', views.edit_room, name ="room"),
    
    path('Registro-clientes/', views.client, name="client" ),    
    path('Clientes/', views.list_client, name="listclients" ),    
    path('Eliminarc/<int:id>', views.clientdelete, name='Eliminarc'),    
    path("Editarc/<int:id>", views.editclient, name="editarc"),
    path("Editarcliente/<int:id>", views.editc, name="Editarcliente"),
    
    
    
    path('Reservaciones/', views.list_booking, name="reservaciones" ),
    path('Eliminar-reservacion/<int:id>',views.bookingdelete, name='Eliminar_reservacion'),
    path("Editarr/<int:id>", views.editbooking, name="editarr"),
    
    #path('register/',views.register, name='register'),F3E9C8
    
    path('Listar-hospedajes/', views.list_guest, name="hospedajes"),
    path('Registrar-reservacion-hospedaje/<int:id>', views.registerguest, name="registrar_hospedaje"),
    path("Editar-hospedaje/<int:id>", views.editguest, name="Editarhospedaje"),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)