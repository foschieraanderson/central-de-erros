export function authHeader() {
    // retorna o header de autorização com JWT token
    let user = JSON.parse(localStorage.getItem("user"));

    if (user && user.token) {
        return { 'Authorization': 'JWT ' + user.token };
    } else {
        return {};
    }
}