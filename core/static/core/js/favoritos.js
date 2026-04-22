// Favoritos functionality - Modal form submission & Drag & Drop

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
    // Modal form AJAX submission
    const favoritoModalForm = document.getElementById('favorito-modal-form');
    if (favoritoModalForm) {
        favoritoModalForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const formData = new FormData(favoritoModalForm);
            const csrftoken = getCookie('csrftoken');

            fetch(favoritoModalForm.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'X-Requested-With': 'XMLHttpRequest',
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Close modal
                    const modal = bootstrap.Modal.getInstance(document.getElementById('addFavoritoModal'));
                    if (modal) modal.hide();

                    // Reload page to show new favorito
                    window.location.reload();
                } else {
                    alert('Erro ao adicionar favorito. Tente novamente.');
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Erro ao adicionar favorito. Tente novamente.');
            });
        });
    }

    // SortableJS for drag & drop (only on favoritos lista page)
    const favoritosSortable = document.getElementById('favoritos-sortable');
    if (favoritosSortable) {
        initializeSortable();
    }
});

// Initialize Sortable (waits for library to load)
function initializeSortable() {
    const favoritosSortable = document.getElementById('favoritos-sortable');
    if (!favoritosSortable) {
        console.log('Favoritos: Container #favoritos-sortable não encontrado');
        return;
    }

    // Wait for Sortable to be available
    if (typeof Sortable === 'undefined') {
        console.log('Favoritos: Aguardando SortableJS carregar...');
        setTimeout(initializeSortable, 100);
        return;
    }

    console.log('Favoritos: Inicializando drag & drop...');
    const sortableInstance = new Sortable(favoritosSortable, {
        animation: 150,
        handle: '.drag-handle',
        ghostClass: 'sortable-ghost',
        onStart: function(evt) {
            console.log('Favoritos: Começou a arrastar item');
        },
        onEnd: function(evt) {
            console.log('Favoritos: Item solto, salvando nova ordem...');
            // Get new order
            const items = favoritosSortable.querySelectorAll('[data-favorito-id]');
            const ordem = Array.from(items).map(item => item.dataset.favoritoId);

            // Send to server
            const csrftoken = getCookie('csrftoken');
            fetch('/favoritos/reordenar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({ ordem: ordem })
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    console.error('Erro ao reordenar');
                    alert('Erro ao salvar ordem. Tente novamente.');
                }
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Erro ao salvar ordem. Tente novamente.');
            });
        }
    });
    console.log('Favoritos: ✓ Drag & drop inicializado com sucesso!');
}
