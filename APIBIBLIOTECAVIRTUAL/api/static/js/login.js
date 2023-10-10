const username = document.getElementById('username').value;
const password = document.getElementById('password').value;

function loginForm(event) {
    event.preventDefault();  // Prevenir la acción por defecto del formulario



    const csrftoken = getCookie('csrftoken');  // Obtener el token CSRF

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Bienvenido");
        
         
        } else {
            alert("Credenciales incorrectas. Por favor, inténtalo de nuevo.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Función para obtener el valor del token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}