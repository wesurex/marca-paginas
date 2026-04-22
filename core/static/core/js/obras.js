// Toggle favorito em obras

// CSRF Token helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
    // Toggle favorito buttons
    const favoritoBtns = document.querySelectorAll('.btn-toggle-favorito');

    favoritoBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            const obraId = this.dataset.obraId;
            const icon = this.querySelector('i');

            // Send AJAX request
            const csrftoken = getCookie('csrftoken');
            fetch(`/ajax/obras/${obraId}/toggle-favorito/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Toggle icon
                    if (data.favorito) {
                        icon.classList.remove('bi-star');
                        icon.classList.add('bi-star-fill');
                        this.classList.add('active');
                    } else {
                        icon.classList.remove('bi-star-fill');
                        icon.classList.add('bi-star');
                        this.classList.remove('active');
                    }
                } else {
                    console.error('Erro ao favoritar:', data.error);
                }
            })
            .catch(error => {
                console.error('Erro:', error);
            });
        });
    });
});
