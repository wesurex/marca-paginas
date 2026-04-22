// AJAX Search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-obras-input');
    const searchResults = document.getElementById('search-results');

    if (!searchInput || !searchResults) return;

    let debounceTimer;

    // Debounce function (300ms delay)
    function debounce(func, delay) {
        return function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(func, delay);
        };
    }

    // Perform search
    function performSearch() {
        const query = searchInput.value.trim();

        if (query.length < 2) {
            searchResults.classList.add('d-none');
            return;
        }

        fetch(`/ajax/obras/search/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                if (data.obras && data.obras.length > 0) {
                    renderResults(data.obras);
                    searchResults.classList.remove('d-none');
                } else {
                    renderNoResults();
                    searchResults.classList.remove('d-none');
                }
            })
            .catch(error => {
                console.error('Erro na busca:', error);
                searchResults.classList.add('d-none');
            });
    }

    // Render search results
    function renderResults(obras) {
        let html = '';
        obras.forEach(obra => {
            const capaHtml = obra.capa_url
                ? `<img src="${obra.capa_url}" alt="${obra.titulo}" class="search-result-capa">`
                : `<div class="search-result-capa-placeholder"><i class="bi bi-book"></i></div>`;

            html += `
                <a href="${obra.url_detalhe}" class="search-result-item">
                    ${capaHtml}
                    <div class="search-result-info">
                        <div class="search-result-title">${obra.titulo}</div>
                        <div class="search-result-meta">
                            <span class="badge bg-secondary">${obra.tipo}</span>
                            ${obra.autor ? `<span class="text-muted ms-2">${obra.autor}</span>` : ''}
                            ${obra.status_leitura ? `<span class="badge bg-info ms-2">${obra.status_leitura}</span>` : ''}
                        </div>
                    </div>
                </a>
            `;
        });
        searchResults.innerHTML = html;
    }

    // Render no results message
    function renderNoResults() {
        searchResults.innerHTML = `
            <div class="search-no-results">
                <i class="bi bi-search"></i>
                <p>Nenhuma obra encontrada</p>
            </div>
        `;
    }

    // Event listener with debounce
    searchInput.addEventListener('input', debounce(performSearch, 300));

    // Close dropdown when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.add('d-none');
        }
    });

    // Show results again when focusing input (if has value)
    searchInput.addEventListener('focus', function() {
        if (searchInput.value.trim().length >= 2) {
            performSearch();
        }
    });
});
