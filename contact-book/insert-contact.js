

function submitForm(e){
   e.preventDefault();

   const form = new FormData(document.querySelector('#editForm'));

   form.append('apiKey',apiKey);

   fetch(rootPath + "controller/insert-contact", {
       method: 'POST',
       headers: {
           'Accept': 'application/json',
       },
       body: form
   })
}