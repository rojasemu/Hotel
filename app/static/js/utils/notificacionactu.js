function actualizarHospedaje(id) {  

    Swal.fire({
    
                title: "¿Confirma Actualizar Hospedaje?",
                showCancelButton: true,                
                confirmButtonText:"Actualizar",
                cancelButtonText:"No,Cancelar",
                confirmButtonColor:"#d33",
                showLoaderOnConfirm:true,           
        
            })

            .then(function(result){

                if (result.isConfirmed){

                    window.location.href = "/Editar-hospedaje/"+id+""
                }
            })



    
}