const searchForm = document.getElementById('search-form');
const contentContainer = document.getElementById('content-container');
const baseEndpoint = "http://localhost:8000/v3";

if (searchForm) {
    searchForm.addEventListener('submit',  handleSearch);
}

function isTokenNotValid(jsonData) {
    if(jsonData.code && jsonData.code === 'token_not_valid'){
        // run a refresh token query

        alert("Please Login Again");
        window.location.href = "http://127.0.0.1:5501/login/index.html";
        return false;
    }
    return true;
}

function handleSearch(event){
    event.preventDefault();

    const cari = document.getElementById('cari').value;

    const endpoint = `${baseEndpoint}/pestisida-pupuk/${cari}`;

    // get access token from local(chaching)
    const authToken = localStorage.getItem('access');

    const options = {
        method: "GET",
        headers: {
            "Content-Type" : "application/json",
            "Authorization" : `Bearer ${authToken}`
        }
    }

    fetch(endpoint, options)
    .then((response) => {
        console.log("respon e: ",response)
        return response.json()
    })
    .then(data => {
        console.log('hasil : ',data);
        const isValidData = isTokenNotValid(data);

        if (isValidData && data){
            let htmlStr = "";
                htmlStr +=  `
                <div class="card mb-3 shadow-sm" id="card">
                    <div class="card-body">
                        <h5 class="card-title">${data.nama_obat}</h5>
                        <p class="card-text"><strong>Jenis      :</strong> ${data.jenis}</p>
                        <p class="card-text"><strong>Produsen   :</strong> ${data.produsen}</p>
                        <p class="card-text"><strong>Warna      :</strong> ${data.warna}</p>
                        <br>
                    </div>
                </div>
            `;

            
            contentContainer.innerHTML = htmlStr
            if (data.length === 0){
                contentContainer.innerHTML = "<p>Pestisida doesn't exist</p>"
            }
        } else {
            contentContainer.innerHTML = "<p>Pestisida doesn't exist</p>"
        }
    })
    .catch((error) =>{
        console.log(error);
    })

}
