
    // Create an object to store usernames and passwords
    const users = {
    '22632514': 'jyotsna124',
    '1000471118': 'kavish86',
    '1000481027': 'venu95',
    '1000472100': 'arnav78',
    '1000513331': 'yatharth250',
    '1000486452': 'mangal174',
    '1000481431': 'aaradhya103',
    '1000472393': 'rounav164',
    '1000469839': 'vedant193',
    '1000508822': 'vedansh170',
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
        window.location.href = 'https://www.hinotes.pythonanywhere.com'; // Redirect to homepage
    }
    } else {
    // If the username is invalid, deny access to the website
    window.location.href = 'https://www.hinotes.pythonanywhere.com'; // Redirect to homepage
    }

