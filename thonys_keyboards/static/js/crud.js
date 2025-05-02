document.addEventListener('DOMContentLoaded', function() {
    const API_URL = 'http://localhost:8000/keyboards';
    const form = document.getElementById('keyboard-form');
    const tableBody = document.querySelector('#keyboards-table tbody');

    // Cargar todos los teclados al iniciar
    loadKeyboards();

    // Manejar envío del formulario
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const keyboardData = {
            name: document.getElementById('name').value,
            // Agrega aquí los demás campos
        };

        const keyboardId = document.getElementById('keyboard-id').value;
        
        try {
            if (keyboardId) {
                await updateKeyboard(keyboardId, keyboardData);
            } else {
                await createKeyboard(keyboardData);
            }
            form.reset();
            loadKeyboards();
        } catch (error) {
            console.error('Error:', error);
        }
    });

    // Cargar teclados
    async function loadKeyboards() {
        try {
            const response = await fetch(API_URL);
            const keyboards = await response.json();
            renderKeyboards(keyboards);
        } catch (error) {
            console.error('Error al cargar teclados:', error);
        }
    }

    // Mostrar teclados en la tabla
    function renderKeyboards(keyboards) {
        tableBody.innerHTML = '';
        keyboards.forEach(keyboard => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${keyboard.name}</td>
                <td>
                    <button class="btn btn-sm btn-warning" onclick="editKeyboard(${keyboard.id})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteKeyboard(${keyboard.id})">Eliminar</button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    }

    // Crear nuevo teclado
    async function createKeyboard(data) {
        await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
    }

    // Actualizar teclado
    async function updateKeyboard(id, data) {
        await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
    }

    // Eliminar teclado
    async function deleteKeyboard(event, id) {
        event.preventDefault();
        if (confirm("¿Eliminar este teclado?")) {
            try {
                const response = await fetch(`/delete/${id}`, {
                    method: 'DELETE'
                });
                if (response.ok) {
                    event.closest('tr').remove();
                }
            } catch (error) {
                console.error("Error:", error);
            }
        }
    }
    // Editar teclado
    window.editKeyboard = async function(id) {
        const response = await fetch(`${API_URL}/${id}`);
        const keyboard = await response.json();
        
        document.getElementById('keyboard-id').value = keyboard.id;
        document.getElementById('name').value = keyboard.name;
        // Completa los demás campos
    };
});