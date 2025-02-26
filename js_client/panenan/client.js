
const contentContainer = document.getElementById('content-container');
const baseEndpoint = "http://localhost:8000/v3";

function isTokenNotValid(jsonData) {
    if(jsonData.code && jsonData.code === 'token_not_valid'){
        // run a refresh token query

        alert("Please Login Again");
        window.location.href = "http://127.0.0.1:5501/login/index.html";
        return false;
    }
    return true;
}

function formatTanggal(dateString) {
    let date = new Date(dateString);  // Konversi string ke objek Date

    let options = { day: 'numeric', month: 'long', year: 'numeric' };
    return new Intl.DateTimeFormat('id-ID', options).format(date);
}

const endpoint = `${baseEndpoint}/panenan/`;

 // get access token from local(chaching)
const authToken = localStorage.getItem('access');

const options = {
        method: "GET",
        headers: {
            "Content-Type" : "application/json",
            "Authorization" : `Bearer ${authToken}`
        }
};

// for (let index = 0; index < 1000; index++) {
    
    


fetch(endpoint, options)
    .then((response) => {
        console.log("respon sebagai berikut: ",response)
        return response.json()
    })
    .then(data => {
        console.log(data.results);
        const isValidData = isTokenNotValid(data);

        if (isValidData && data.results){
            let htmlStr = "";
            for (let result of data.results){   
                
                htmlStr +=  `
                <div class="card mb-3 shadow-sm" id="card">
                    <div class="card-body">
                        <h5 class="card-title">${result.tanaman_nama}</h5>
                        <p class="card-text"><strong>Tanggal:</strong> ${formatTanggal(result.tanggal_panen)}</p>
                        <p class="card-text"><strong>Berat:</strong> ${result.berat_ton} ton</p>
                        <p class="card-text"><strong>Total Pendapatan:</strong> Rp${result.total_harga.toLocaleString("id-ID")}</p>
                        <p class="card-text"><strong>Waktu Tanam:</strong> ${result.waktu_tanam} hari</p>
                        <p class="card-text"><strong>Pemanen:</strong> ${result.petani}</p>
                        <br>
                    </div>
                    
                    
                </div>
            `;

            }
            contentContainer.innerHTML = htmlStr
            if (data.results.length === 0){
                contentContainer.innerHTML = "<p>Tidak Ada  Panenan</p>"
            }
        } else {
            contentContainer.innerHTML = "<p>Tidak Ada Panenan</p>"
        }
    })
    .catch((error) =>{
        console.log(error);
});

// }

// for (let index = 0; index < 1000000; index++) {
//     fetch(endpoint, options)
// }

// console.log("Success test");



