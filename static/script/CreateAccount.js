let senha = document.getElementById("senha");
let senhaConfirmar = document.getElementById("senhaConfirmar");
let submit = document.getElementById("submit");

 function verificaSenhaConfirmar()  { 
    console.log('batata')
    
}


senha.onkeyup = function() {
    s1 = senha.value
    s2 = senhaConfirmar.value
    if (s1 != s2) {
        submit.disabled = true;
    } 
    if (senha.value == senhaConfirmar.value) {
        submit.disabled = false;  
    }
}

//eu estava mexendo nisso. É um script para impedir o usuário de confirmar o cadastro se
//as senhas que ele escrever não estiverem iguais. Não está funcionando