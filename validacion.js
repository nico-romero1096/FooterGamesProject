function validar(){
    let mail = document.getElementById("mail");
    let pass = document.getElementById("pass");
    let error = false;
    document.getElementById("validar_mail").innerHTML = "&nbsp; "

    if (mail.value == ""){
        document.getElementById("validar_mail").innerHTML = "Debe completar el mail"
        error = true
        mail.focus()
    }
    
    if (pass.value.length <8){
        document.getElementById("validar_pass").innerHTML = "Debe completar la contraseña"
        error = true
        pass.focus()
    }

    if (error == false){
        document.getElementById("mail").value = ""
        document.getElementById("validar_mail").innerHTML = "&nbsp;"
        document.getElementById("pass").value = ""
        document.getElementById("validar_pass").innerHTML = "&nbsp"
        alert("Dato enviado")
    }
    return !error


}