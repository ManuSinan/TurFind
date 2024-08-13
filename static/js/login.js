document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    const popup = document.getElementById('error-popup');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Send a request to the server to check the credentials
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.valid) {
                // Show the popup if the credentials are invalid
                popup.style.display = 'block';
            } else {
                // Redirect to the dashboard or whatever page you want
                window.location.href = '/dashboard';
            }
        })
        .catch(error => console.error(error));
    });

    // Add an event listener to close the popup
    document.querySelector('.close-popup').addEventListener('click', () => {
        popup.style.display = 'none';
    });
});
