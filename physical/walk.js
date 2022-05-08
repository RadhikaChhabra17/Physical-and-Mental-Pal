// function retrieveName (e) {
//     e.preventDefault()

//     let username = document.getElementById('uname').value

//     fetch(`http://127.0.0.1:5000/${username}`)
//     .then((res)=> res.json())
//     .then((data)=> {
//         document.getElementById('output').innerHTML = `<li class="list-group-item">"Login successfully!"</li> `
//     })
// }


document.getElementById('walkData').addEventListener('submit', walkData)

function walkData (e) {
    e.preventDefault()

    let username = document.getElementById('uname').value
    let duration = document.getElementById('q1').value
    let distance = document.getElementById('q2').value
    let preference = document.getElementById('q3').value
    
   
    fetch('http://127.0.0.1:5000/walkData', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'uname' : username,
            'q1' : duration,
            'q2' : distance,
            'q3' : preference
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}