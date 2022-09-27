let senha = document.getElementById("senha");
let senhaConfirmar = document.getElementById("senhaConfirmar");
let submit = document.getElementById("submit");



 function verificaSenhaConfirmar()  { 
    console.log('batata')
    if (senha.textContent != senhaConfirmar.textContent) {
        submit.disabled = True;
    } else if (senha.textContent == senhaConfirmar.textContent) {
        submit.disabled = False;  
    }
}

//testes