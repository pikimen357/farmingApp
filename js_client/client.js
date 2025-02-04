const loginForm = document.getElementById('login-form');
const baseEndpoint = "http://localhost:8000/";

if (loginForm) {
    loginForm.addEventListener('submit',  handleLogin);
}

function handleLogin(event){
    console.log(event);
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}api/token/`;

    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyStr);

    const options = {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: bodyStr
    }

    fetch(loginEndpoint, options)
    .then((response) => {
        console.log("respon e: ",response)
        return response.json()
    })
    .then(handleAuthData)
    .catch((error) =>{
        console.log(error);
    })

}

// storing access and refresh token in local storage
function handleAuthData(authData) {
    localStorage.setItem('access', authData.access);
    localStorage.setItem('refresh', authData.refresh);
}

function getProductList() {
    const endpoint = `${baseEndpoint}v3/products/`;
    const options = {
        method: "GET",
        headers: {
            "Content-Type" : "application/json"
        }
        
    }

    fetch(endpoint, options)
    .then(response=>response.json())
    .then(data => {

    })
}