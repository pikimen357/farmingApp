const tanamanForm = document.getElementById('tanamanForm');
const warningHarga = document.getElementById('warning-harga');
const warningWaktu = document.getElementById('warning-waktu');

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

const dataHama =  document.getElementById('peluang_hama');

const opt = {
    method : "GET",
    headers : {
        "Content-Type" : "application/json",
        "Authorization" : `Bearer ${authToken}`
    }
}


fetch('http://localhost:8000/v3/hama/', opt)
.then((response) => {
    console.log(`Responnya : ${response}`);
    return response.json();
})
.then((data) => {
    // const isValidData = isTokenNotValid(data);
        console.log(data);
        if (data.results.length != 0) {
            let htmlStr = '';
            for (let result of data.results){
                console.log(result);
                htmlStr += `<option value=${result.id}>${result.nama_hama}`;
            }
            dataHama.innerHTML = htmlStr;
        } else {
            dataHama.innerHTML = '<option value="Tidak ada hama"></option>';
        }

})
.catch(error => console.log("Errornya : ",error));

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
                
                console.log('Response:', data);
                // Redirect ke halaman sukses atau reset form
                warningHarga.innerHTML = `<p>${data.harga_perTon[0]}</p>`
                warningWaktu.innerHTML = `<p>${data.waktu_tanam_hari[0]}</p>`
                document.getElementById('tanamanForm').reset();
        } 
        else {
            alert('Data berhasil dikirim!');
            // alert('Gagal mengirim data: ' + (data.message || 'Unknown error'));
            // console.error('Error response:', data);
        }
    })
    .catch(error => alert('Terjadi kesalahan: ' + error));
});