document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('paymentForm').addEventListener('submit', function(event) {
        const cardNumber = document.getElementById('ccnum').value.replace(/-/g, '');
        const expMonth = document.getElementById('expmonth').value;
        const expYear = document.getElementById('expyear').value;
        const cvv = document.getElementById('cvv').value;

        // Validate card number
        if (!/^\d{10}$/.test(cardNumber)) {
            alert('Please enter a valid card number.');
            event.preventDefault();
            return;
        }

        if (!/^\d{4}$/.test(expYear) || expYear < currentYear || (expYear == currentYear && expMonth < currentMonth)) {
            alert('Please enter a valid expiration year.');
            event.preventDefault();
            return;
        }

    });
});
