
    // Create an object to store usernames and passwords
    const users = {
        'admin': 'chirag',
        'jyotsna': '124',
        };
    
        // Prompt the user for their username
        const username = prompt('Enter your username:');
    
        // Check if the username is valid
        if (username in users) {
        // If the username is valid, prompt the user for their password
        const password = prompt('Enter your password:');
        
        // Check if the password is correct
        if (password === users[username]) {
            // If the password is correct, allow access to the website
        } else {
            // If the password is incorrect, deny access to the website
            window.location.href = 'https://www.HiNotes.pythonanywhere.com'; // Redirect to homepage
        }
        } else {
        // If the username is invalid, deny access to the website
        window.location.href = 'https://www.HiNotes.pythonanywhere.com'; // Redirect to homepage
        }
    
    