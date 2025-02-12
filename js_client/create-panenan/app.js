const panenanForm = document.getElementById('panenanForm');
const dataTanaman = document.getElementById('tanaman-list');

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

const options = {
    method: "GET",
    headers: {
        "Content-Type" : "application/json",
        "Authorization" : `Bearer ${authToken}`
    }
};


// get all tanaman, then add to <datalist>
 fetch('http://127.0.0.1:8000/v3/tanaman/', options)    
 .then((response) => {
    console.log("respon e: ",response);
    return response.json();
})
.then((data) => {
    console.log(data.results);
    const isValidData = isTokenNotValid(data);

    if (isValidData && data.results){
        let htmlStr = "";
        for (let result of data.results){   
            console.log(result);
            htmlStr +=  `
                <option value="${result.id}">${result.nama_tanaman}</option>
        `;
        }
        dataTanaman.innerHTML = htmlStr
        if (data.results.length === 0){
            dataTanaman.innerHTML = '<option value="Tidak ada tanaman"></option>'
        }
    }
    else {
        dataTanaman.innerHTML = '<option value="Tidak ada tanaman"></option>'
    }

})
.catch(error => alert('Terjadi kesalahan: ' + error));



 panenanForm.addEventListener('submit', function(event) {
    event.preventDefault();

    let panenanFormData = new FormData(panenanForm);
    let panenanObjectData = Object.fromEntries(panenanFormData);
    let bodyStr = JSON.stringify(panenanObjectData);
    console.log("bodystr : ",bodyStr);
    
    fetch('http://127.0.0.1:8000/v3/panenan-create/', {
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