const $formr_and_h= document.getElementById('formr_and_h');
const $dinerorecibido = document.getElementById('dinerorecibido');
const $detallepago = document.getElementById('detallepago');
const $deudacliente = document.getElementById('deudacliente');
const $deudahotel = document.getElementById('deudahotel');
const $total = document.getElementById('total');





(function() {   

     $formr_and_h.addEventListener('submit', function (e){
          let dinerorecibido = String($dinerorecibido.value).trim();         
          let detallepago = String($detallepago.value).trim();         
          let deudacliente = String($deudacliente.value).trim();                          
          let deudahotel = String($deudahotel.value).trim();         
          let total = String($total.value).trim();         
               
          
          
     
          if ( dinerorecibido.length==0 || detallepago .length==0 || deudacliente.length==0 ||  deudahotel.length==0  || total.length==0 ){
     
               alert ("No puede dejar campos en blanco...")
               e.preventDefault();
     
          }     
     });
         
}) ();
