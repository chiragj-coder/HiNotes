
// Create an object to store usernames and passwords
const users = {
    'teacher': 'iamteacher','22632514': 'jyotsna124','1000481431': 'aaradhya103','1000513331': 'yatharth250','1000471118': 'kavish86','1000486452': 'mangal174','1000472393': 'rounav164','1000481027': 'venu95','1000472100': 'arnav78','1000469839': 'vedant193','1000508822': 'vedansh170','1000482880': 'aaditya166', '1000487928': 'abhay165', '1000352043': 'amay108', '1000483504': 'anshika97', '1000472100': 'arnav78', '1000510373': 'ayush137', '1000506763': 'azfaar190', '1000469740': 'hritom193', '1000478810': 'ishita155','1000352080': 'maitri145', '1000473652': 'ojasv145', '1000483098': 'piyush186', '1000480445': 'prachi107', '1000466838': 'pramiti162', '1000475934': 'prathvi150', '_01000472730': 'prayag114', '1000472452': 'riddhima133', '1000479462': 'rishu213', '1000473327': 'shivansh117', '1000481737': 'shourya112', '_01000480714': 'shrigopal79', '_01000473344': 'sonam134', '1000469248': 'soumy196', '1000352081': 'tanishka146', '1000508822': 'vedansh170', '_01000469839': 'vedant193', '1000481027': 'venu95',
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

