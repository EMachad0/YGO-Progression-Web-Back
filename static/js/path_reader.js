const path = window.location.pathname.split('/');
console.log(path)

function get_guild() {
    return path[2];
}

function get_user() {
    return path[3];
}