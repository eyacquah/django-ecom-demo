 var updateBtn = document.getElementsByClassName('update_cart')

for (var i = 0; i < updateBtn.length; i++){
  updateBtn[i].addEventListener('click', function(){
    var productPk = this.dataset.product
    var action = this.dataset.action
    console.log('productPk:', productPk, 'action:', action)

    console.log('USER:', user)
    if (user === 'AnonymousUser') {
      console.log('Not logged in')
    } else {
      updateUserOrder(productPk, action)
    }
  })
}

function updateUserOrder(productPk, action){
  console.log('Logged in! Sending data...')

  var url = '/update/'

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({'productPk': productPk, 'action': action})
  })
  .then((response) =>{
    return response.json()
  })
  .then((data)=>{
    console.log('data:', data)
    location.reload()
  })
}
