
document.getElementById('submitForm').addEventListener('click', submitForm);

document.getElementById('cancelButton').addEventListener('click', function() {
   window.open("index.html", "_self");
}
);


function submitForm(e){
   e.preventDefault();

   const form = new FormData(document.querySelector('#editForm'));

   form.append('apiKey',apiKey);

   fetch(rootPath + "controller/insert-contact/", {
       method: 'POST',
       headers: {
           'Accept': 'application/json,*.*'
       },
       body: form
   })   

   .then(function(response){
    return response.text();
   })
   .then(function(data){
       if (data === "success") {
           alert("Contact added successfully!");
           window.open("index.html", "_self");
       } else {
           alert("Error adding contact: " + data);
       }
   })   
}