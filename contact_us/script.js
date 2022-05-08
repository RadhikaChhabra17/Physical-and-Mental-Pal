var card = document.getElementById("card");

function openSignUp(){
    card.style.transform= "rotateY(-180deg)";
    }
    function openLOGIN(){
    card.style.transform= "rotateY(0deg)";
    }
// document.getElementById('formData').addEventListener('submit', retrieveName)

// function retrieveName (e) {
//     e.preventDefault()

//     let name = document.getElementById('name').value
    


//     fetch(`http://127.0.0.1:5000/${name}`)
//     .then((res)=> res.json())
//     .then((data)=> {
//         document.getElementById('output').innerHTML = `<li class="list-group-item">"Login successfully!"</li> `
//     })
// }


document.getElementById('postData').addEventListener('submit', postData)

function postData (e) {
    e.preventDefault()

    let name = document.getElementById('postName').value
    let email = document.getElementById('postEmail').value
    let message = document.getElementById('postMessage').value
    
   
    fetch('http://127.0.0.1:5000/postData', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'name' : name,
            'email' : email,
            'message' : message    
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}

function func() {
    var frm = document.getElementsByName('contact-form')[0];
   frm.submit(); // Submit the form
   frm.reset();  // Reset all form data
   return false; // Prevent page refresh
  }