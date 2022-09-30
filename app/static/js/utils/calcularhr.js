let precio_habitacion = 0;
          let cantidad_adicionall = 0;
          let cantidad_check_in = 0;
          let cantidad_check_out = 0;
          let cantidad_total_extras = 0;
          let total_general = 0;
          let deuda_client = 0;
          let favor = 0;
          let dias = 0;
          let extrain = 0;
          let extraout = 0;
          let extraadi = 0;

        function calculo_dias(){
            var aFecha1 = document.getElementById("fechaentrada").value .split('-');
            var aFecha2 = document.getElementById("fechasalida").value .split('-');
            var fFecha1 = Date.UTC(aFecha1[0],aFecha1[1]-1,aFecha1[2]);
            var fFecha2 = Date.UTC(aFecha2[0],aFecha2[1]-1,aFecha2[2]);
            var dif = fFecha2 - fFecha1;
            dias = Math.floor(dif / (1000 * 60 * 60 * 24));
        }

        function dineros (){
            if(deuda_client < 0){
                document.getElementById("deudacliente").value = 0
           }
           else{
                document.getElementById("deudacliente").value = deuda_client
           }

           if(favor < 0) {
                document.getElementById("deudahotel").value = 0
           }
           else{
                document.getElementById("deudahotel").value = favor
           }
        }

     function calculo_habitacion() {
          precio_habitacion = (document.getElementById("habitacion").value).split(',')

          if(!cantidad_adicionall) calculo_cant_adicional()
          if(!cantidad_check_in) calculo_cant_extrain()
          if(!calculo_cant_extraout) calculo_cant_extraout()

          if(document.getElementById("fechasalida").value){

                calculo_dias()

                if(cantidad_total_extras) total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                else total_general = (precio_habitacion[1] * dias) + 0;

                document.getElementById("total").value = total_general;

                deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                favor = (document.getElementById("dinerorecibido").value) - (total_general);
                dineros ()
          }
          else{
               total_general = 0;
               document.getElementById("total").value = total_general;
          }
     }

     function calculo_cant_adicional(){
            if(document.getElementById("cantidad_adicional").value != ''){
                if(document.getElementById("fechasalida").value){
                    if(!cantidad_total_extras && extrain==0 && extraout==0){
                         extraadi = 1
                         calculo_cant_extrain()
                         calculo_cant_extraout()
                         precio_habitacion = (document.getElementById("habitacion").value).split(',')
                         calculo_dias()               
                    }
                    
                    if(!cantidad_adicionall){
                         cantidad_adicionall = document.getElementById("precio_cantidad_adicional").value * document.getElementById("cantidad_adicional").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_adicionall
                     
                    } 
                    else{
                         
                         cantidad_total_extras = cantidad_total_extras - cantidad_adicionall
                         cantidad_adicionall = document.getElementById("precio_cantidad_adicional").value * document.getElementById("cantidad_adicional").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_adicionall
                    }

                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);

                    dineros()
               }
               else{
                    cantidad_adicionall = document.getElementById("precio_cantidad_adicional").value * document.getElementById("cantidad_adicional").value;
                    cantidad_total_extras = cantidad_total_extras + cantidad_adicionall
                    total_general = 0;
                    document.getElementById("total").value = total_general;
               }
            }
            else{
                if(document.getElementById("fechasalida").value){
                    calculo_dias()
                    cantidad_total_extras = cantidad_total_extras - cantidad_adicionall
                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);
                    dineros()
                }
                else{
                    cantidad_total_extras = cantidad_total_extras - cantidad_adicionall
                    total_general = 0 + cantidad_total_extras;
                    document.getElementById("total").value = total_general;
                }
            }
        }

     function calculo_cant_extrain(){
            if(document.getElementById("cantidad_in").value != ''){
                if(document.getElementById("fechasalida").value){

                    if(!cantidad_total_extras && extraadi==0 && extraout==0){
                         extrain = 1
                         calculo_cant_adicional()
                         calculo_cant_extraout()
                         precio_habitacion = (document.getElementById("habitacion").value).split(',')
                         calculo_dias()               
                    }

                    if(!cantidad_check_in){
                         cantidad_check_in = document.getElementById("extra_check_in").value * document.getElementById("cantidad_in").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_check_in 
                    } 
                    else{
                         cantidad_total_extras = cantidad_total_extras - cantidad_check_in
                         cantidad_check_in = document.getElementById("extra_check_in").value * document.getElementById("cantidad_in").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_check_in 
                    }


                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);

                    dineros()
               }
               else{
                    cantidad_check_in = document.getElementById("extra_check_in").value * document.getElementById("cantidad_in").value;
                    cantidad_total_extras = cantidad_total_extras + cantidad_check_in 
                    total_general = 0;
                    document.getElementById("total").value = total_general;
               }
            }
            else{
                if(document.getElementById("fechasalida").value){
                    calculo_dias()
                    cantidad_total_extras = cantidad_total_extras - cantidad_check_in
                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);
                    dineros()
                }
                else{
                    cantidad_total_extras = cantidad_total_extras - cantidad_check_in
                    total_general = 0 + cantidad_total_extras;
                    document.getElementById("total").value = total_general;
                }
            }
        }

     function calculo_cant_extraout(){
            if(document.getElementById("cantidad_out").value != ''){
                if(document.getElementById("fechasalida").value){

                    if(!cantidad_total_extras && extraadi==0 && extrain==0){
                         extraout = 1
                         calculo_cant_adicional()
                         calculo_cant_extrain()
                         precio_habitacion = (document.getElementById("habitacion").value).split(',')
                         calculo_dias()               
                    }

                    if(!cantidad_check_out){
                         cantidad_check_out = document.getElementById("extra_check_out").value * document.getElementById("cantidad_out").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_check_out 
                    } 
                    else{
                         cantidad_total_extras = cantidad_total_extras - cantidad_check_out
                         cantidad_check_out = document.getElementById("extra_check_out").value * document.getElementById("cantidad_out").value;
                         cantidad_total_extras = cantidad_total_extras + cantidad_check_out 
                    }

                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);

                    dineros()
               }
               else{
                    cantidad_check_out = document.getElementById("extra_check_out").value * document.getElementById("cantidad_out").value;
                    cantidad_total_extras = cantidad_total_extras + cantidad_check_out
                    total_general = 0;
                    document.getElementById("total").value = total_general;
               }
            }
            else{
                if(document.getElementById("fechasalida").value){
                    calculo_dias()
                    cantidad_total_extras = cantidad_total_extras - cantidad_check_out
                    total_general = (precio_habitacion[1] * dias) + cantidad_total_extras;
                    document.getElementById("total").value = total_general;

                    deuda_client = (total_general) - (document.getElementById("dinerorecibido").value);
                    favor = (document.getElementById("dinerorecibido").value) - (total_general);
                    dineros()
                }
                else{
                    cantidad_total_extras = cantidad_total_extras - cantidad_check_out
                    total_general = 0 + cantidad_total_extras;
                    document.getElementById("total").value = total_general;
                }
            }
        }
               
     function calculo_total(){

          if(document.getElementById("fechasalida").value){
               calculo_habitacion()
          }
          else{
               total_general = 0;
               document.getElementById("total").value = total_general;
          }
     }

     function deuda_cliente(){
          calculo_habitacion()
     }