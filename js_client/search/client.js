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


    const endpoint = `${baseEndpoint}/search/tanaman/?${searchParams}`;

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
                <div class="card mb-3 shadow-sm" id="card">
                    <div class="card-body">
                        <h5 class="card-title">${result.nama_tanaman}</h5>
                        <p class="card-text"><strong>Owner:</strong> ${result.owner}</p>
                        <p class="card-text"><strong>Jenis:</strong> ${result.jenis}</p>
                        <p class="card-text"><strong>Harga /ton:</strong> Rp${result.harga_perTon.toLocaleString("id-ID")}</p>
                        <p class="card-text"><strong>Waktu Tanam:</strong> ${result.waktu_tanam_hari} hari</p>
                        <p class="card-text"><strong>Deskripsi:</strong> ${result.deskripsi}.</p>
                        <img src="${result.link_tanaman}" class="card-img-top img-fluid mx-auto d-block mt-3" 
                            alt="${result.nama_tanaman}" style="width: 220px; height:180px; object-fit: cover;">
                        <a href="${result.edit_url}" id="edit-btn" class="btn btn-primary w-100">Edit</a>
                        <br>
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
