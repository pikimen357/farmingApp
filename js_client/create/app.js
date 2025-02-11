const tanamanForm = document.getElementById('tanamanForm');

function isTokenNotValid(jsonData) {
    if(jsonData.code && jsonData.code === 'token_not_valid'){
        // run a refresh token query

        alert("Please Login Again");
        window.location.href = "http://127.0.0.1:5501/login/index.html";
        return false;
    }
    return true;
}

 // get access token from local(chaching)
 const authToken = localStorage.getItem('access');

document.getElementById('tanamanForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let tanamanFormData = new FormData(tanamanForm);
    let tanamanObjectData = Object.fromEntries(tanamanFormData);
    let bodyStr = JSON.stringify(tanamanObjectData);
    console.log("bodystr : ",bodyStr);
    
    fetch('http://127.0.0.1:8000/v3/tanaman/', {
        method: 'POST',
        headers: {
            "Authorization" : `Bearer ${authToken}`,
            'Content-Type': 'application/json'
            
        },
        body: bodyStr
    })
    .then(response => response.json())
    .then(data => {
        const isValid = isTokenNotValid(data);
        if (isValid) {
                alert('Data berhasil dikirim!');
                console.log('Response:', data);
                // Redirect ke halaman sukses atau reset form
                document.getElementById('tanamanForm').reset();
        } 
        else {
            alert('Gagal mengirim data: ' + (data.message || 'Unknown error'));
            console.error('Error response:', data);
        }
    })
    .catch(error => alert('Terjadi kesalahan: ' + error));
});