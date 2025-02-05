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

    let formData = new FormData(searchForm);
    let data = Object.fromEntries(formData);
    let searchParams = new URLSearchParams(data);


    const endpoint = `${baseEndpoint}/search/?${searchParams}`;

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
        console.log(data.results);
        const isValidData = isTokenNotValid(data);

        if (isValidData && data.results){
            let htmlStr = "";
            for (let result of data.results){   
                
                htmlStr +=  `
                <div class="card mb-3 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">${result.nama_tanaman}</h5>
                        <p class="card-text"><strong>Petani id:</strong> ${result.owner}</p>
                        <p class="card-text"><strong>Jenis:</strong> ${result.jenis}</p>
                        <p class="card-text"><strong>Harga /ton:</strong> ${result.harga_perTon}</p>
                        <p class="card-text"><strong>Waktu Tanam:</strong> ${result.waktu_tanam_hari} hari</p>
                    </div>
                </div>
            `;

            }
            contentContainer.innerHTML = htmlStr
            if (data.results.length === 0){
                contentContainer.innerHTML = "<p>Mboten Wonten Tanduran</p>"
            }
        } else {
            contentContainer.innerHTML = "<p>Mboten Wonten Tanduran</p>"
        }
    })
    .catch((error) =>{
        console.log(error);
    })

}
