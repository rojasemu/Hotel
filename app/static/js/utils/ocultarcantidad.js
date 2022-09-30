function comprobar(obj)
{   
    if (obj.checked){
      
document.getElementById('cantidad_adicional').style.display = "";
document.getElementById('cantidad').style.display = "";
   } else{
      
document.getElementById('cantidad_adicional').style.display = "none";
document.getElementById('cantidad').style.display = "none";
   }  
}
function comprobarin(obj) 
{  
    if (obj.checked){
      
document.getElementById('cantidad_in').style.display = "";
document.getElementById('cantidadin').style.display = "";
   } else{
      
document.getElementById('cantidad_in').style.display = "none";
document.getElementById('cantidadin').style.display = "none";
   }
}
function comprobarout(obj) 
{       
    if (obj.checked){
      
document.getElementById('cantidad_out').style.display = "";
document.getElementById('cantidadout').style.display = "";
   } else{
      
document.getElementById('cantidad_out').style.display = "none";
document.getElementById('cantidadout').style.display = "none";
   }     
}