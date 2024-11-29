function deletePhone(phoneId) {
    fetch(`/phones/delete/${phoneId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector(`tr[data-id="${phoneId}"]`).remove();
            }
        });
}

function addPhone() {
    // Implement the logic to add a new phone using AJAX.
}

function filterPhones() {
    const input = document.getElementById('search').value.toLowerCase();
    const rows = document.querySelectorAll('#phoneTable tbody tr');

    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        const matches = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(input));

        row.style.display = matches ? '' : 'none';
    });
}

function exportData(format) {
    const visibleIds = Array.from(document.querySelectorAll('#phoneTable tbody tr'))
        .filter(row => row.style.display !== 'none') // Only include visible rows
        .map(row => row.getAttribute('data-id')) // Get their IDs
        .filter(id => id); // Filter out any empty IDs

    let url = `/phones/export/${format}/?`;

    if (visibleIds.length > 0) {
        url += `ids=${visibleIds.join(',')}`; // Append visible IDs
    }

    window.location.href = url;
}


function saveNewPhone() {
    const brandName = document.getElementById('new-brand').value;
    const model = document.getElementById('new-model').value;
    const price = document.getElementById('new-price').value;
    const color = document.getElementById('new-color').value;
    const displaySize = document.getElementById('new-display-size').value;
    const madeIn = document.getElementById('new-made-in').value;
    const isAvailable = document.getElementById('new-is-available').checked;

    fetch('/phones/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            brand_name: brandName,
            model: model,
            price: price,
            color: color,
            display_size: displaySize,
            made_in: madeIn,
            is_available: isAvailable
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const newRow = `
                <tr data-id="${data.phone.id}">
                    <td>${data.phone.id}</td>
                    <td>${data.phone.brand}</td>
                    <td>${data.phone.model}</td>
                    <td>${data.phone.price}</td>
                    <td>${data.phone.color}</td>
                    <td>${data.phone.display_size}</td>
                    <td>${data.phone.made_in}</td>
                    <td>${data.phone.is_available ? 'True' : 'False'}</td>
                    <td><button onclick="deletePhone(${data.phone.id})">Delete</button></td>
                </tr>`;

                // Insert the new row before the add phone row
                const addRow = document.getElementById('add-phone-row');
                addRow.insertAdjacentHTML('beforebegin', newRow);

                // Clear input fields after saving
                document.getElementById('new-brand').value = '';
                document.getElementById('new-model').value = '';
                document.getElementById('new-price').value = '';
                document.getElementById('new-color').value = '';
                document.getElementById('new-display-size').value = '';
                document.getElementById('new-made-in').value = '';
                document.getElementById('new-is-available').checked = false; // Reset checkbox
            } else {
                // Show detailed error messages from server response
                let errorMessage = "Errors:\n";
                for (const [field, messages] of Object.entries(data.errors)) {
                    errorMessage += `${field}: ${messages.join(', ')}\n`;
                }
                alert(errorMessage);
            }
        });
}


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
