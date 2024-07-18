document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const gender = document.querySelector('input[name="gender"]:checked');
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirm_password').value.trim();
    const checkbox = document.getElementById('check').checked;
    
    if (!name || !email || !phone || !gender || !password || !confirmPassword) {
        alert('Please fill in all fields.');
        return;
    }
    
    
    if (!validatePhone(phone)) {
        alert('Please enter a valid phone number.');
        document.getElementById('phone').value = '';
        return;
    }
    
    if (password !== confirmPassword) {
        alert('Passwords do not match.');
        document.getElementById('password').value = '';
        document.getElementById('confirm_password').value = '';
        return;
    }
    
    if (!checkbox) {
        alert('Please confirm that the details provided are correct.');
        return;
    }
    
    // If all validations pass, submit the form
    document.getElementById('form').submit();
    // You can submit the form data to the server here
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePhone(phone) {
    const re = /^\d{10}$/;
    return re.test(phone);
}
