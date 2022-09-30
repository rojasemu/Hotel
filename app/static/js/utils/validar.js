const $formcliente= document.getElementById('formcliente');
const $name = document.getElementById('name');
const $last_name = document.getElementById('last_name');
const $document_number = document.getElementById('document_number');
const $phone = document.getElementById('phone');

(function() {
     
     //notificacionSwal(document.title, "Clientes Listados con exito", "success", "OK");

     $formcliente.addEventListener('submit', function (e){
          let name = String($name.value).trim();         
          let last_name = String($last_name.value).trim();         
          let document_number = String($document_number.value).trim();                          
          let phone = String($phone.value).trim();         
               
          
          
     
          if ( name.length==0 || last_name.length==0 || document_number.length==0 ||  phone.length==0 ){

               notificacionSwal("Registro Cliente", "No puede dejar campos en blanco...", "warning", "OK");               
               e.preventDefault();
          
     
          }
             
     });
         
}) ();
