const panenanForm = document.getElementById('panenanForm');
const dataTanaman = document.getElementById('tanaman-list');
const warningBerat = document.getElementById('warning-berat-ton');
const warningTanggal = document.getElementById('warning-tanggal')

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
    const isValidData = isTokenNotValid(data);

    if (isValidData && data.results){
        let htmlStr = "";
        for (let result of data.results){   
            console.log(result);
            htmlStr +=  `
                <option value=${result.id}>${result.nama_tanaman}</option>
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
.catch(error => {
    console.log('Terjadi kesalahan: ' + error);
    dataTanaman.innerHTML = '<option value="Tidak ada tanaman"></option>'
});



 panenanForm.addEventListener('submit', function(event) {
    event.preventDefault();

    // make sure there is name=“{json data attribute}” in the html input ===>> FormData
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
    .then((response) => {
        
        console.log("Responsss -->> ", response);
        return response.json();
        // alert('Data berhasil dikirim!');
    })
    .then(data => {
        console.log(data);
        const isValid = isTokenNotValid(data);
        if (isValid) {
            console.log("Responnya ->> ");
            if (data.berat_ton[0]){
                warningBerat.innerHTML = `<p>${data.berat_ton[0]}</p>`;
            }

            if (data.tanggal_panen[0]){
                warningTanggal.innerHTML = `<p>${data.tanggal_panen[0]}</p>`;
            }
            panenanForm.reset();
        } 
        else {
            alert("Data  berhasil dikirim")
        }
    })
    .catch(error => {
        console.log('Terjadi kesalahan: ' + error)

    });
});