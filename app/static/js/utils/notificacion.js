function eliminarCliente (id) {
    
    Swal.fire({
            
                title: "¿Confirma Eliminar Cliente?",
                showCancelButton: true,                
                confirmButtonText:"Eliminar",
                cancelButtonText:"No, Cancelar",
                confirmButtonColor:"#d33",
                showLoaderOnConfirm:true,           
            
            })

            .then(function(result){

                if (result.isConfirmed){

                    window.location.href = "/Eliminarc/"+id+""
                }
            })



            
}

function eliminarReserva (id) {   

    Swal.fire({
    
                title: "¿Confirma Eliminar Reservación?",
                showCancelButton: true,                
                confirmButtonText:"Eliminar",
                cancelButtonText:"No, Cancelar",
                confirmButtonColor:"#d33",
                showLoaderOnConfirm:true,           
            
         })

        .then(function(result){

            if (result.isConfirmed){

                window.location.href = "/Eliminar-reservacion/"+id+""
            }
        })



    
}

