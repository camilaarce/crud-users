import Swal from "sweetalert2";
import axios from "axios";

export function show_alert(mensaje, icono, foco = '') {
    if (foco !== '') {
        document.getElementById(foco).focus();
    }
    Swal.fire({
        title: mensaje,
        icon: icono,
        customClass: { confirmButton: 'btn btn-primary', popup: 'animated zoomIn' },
        buttonsStyling: false,
    }).then(function () {
        window.location = "/";
    });
}

export function eliminar(id, name) {
    var url = 'http://127.0.0.1:8000/users/' + id;
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: { confirmButton: 'btn btn-success me-3', cancelButton: 'btn btn-danger' }
        , buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
        title: '¿Estás seguro de eliminar el usuario ' + name + '?',
        text: 'Se perderá la información del usuario',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: '<i class="fa-solid fa-check"></i> Si, eliminar',
        cancelButtonText: '<i class="fa-solid fa-ban"></i> Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            axios.delete(url);
            show_alert('Usuario eliminado', 'success')
        } else {
            show_alert('Operación cancelada', 'info');
        }
    })
}

export function crear(user) {
    var url = 'http://127.0.0.1:8000/users/';
    axios.post(url, user);
    show_alert('Usuario guardado', 'success');
}

export function editar(id, user) {
    var url = 'http://127.0.0.1:8000/users/' + id;
    axios.put(url, user);
    show_alert('Usuario editado', 'success');
}