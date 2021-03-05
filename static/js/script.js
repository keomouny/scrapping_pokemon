console.log('hello1');
// document.querySelectorAll('#image').forEach(e=>{
//     e.innerHTML = e.innerText });

const url_api = 'http://localhost:5000/api/query_data/header_articles';

async function getData(url) {
    const response = await fetch(url);
    let data = await response.json()
    console.log(data);
    return;
}

getData(url_api);

// fetch('http://localhost:5000/api/query_data/header_articles', {mode: 'cors'}).then(function(response){
//     console.log(response);
//     return response.json()
// }).then(function(data){
//     console.log('my data', data);
// }).catch(function(err){
//     console.log(err)
// })