// Función para crear el contenido del header
function createHeader() {
    const header = document.getElementById('header');
    const headerContent = document.createElement('header');
    headerContent.innerHTML = '<nav id="ancla" class="ancla"><img id ="logo" src="imagenes/logo4.png" alt="logo"> <form action="" class="box"><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li id="register"><a href="registro.html">Registro</a></li></ul><input type="text" name="buscar" id="buscar" placeholder="Buscar..."><a href="login.html" class="box2"><img id="imagen-login" src="./imagenes/persona2.png" alt="persona"></a></form> ';
    header.appendChild(headerContent);
}

// Función para crear el contenido del footer
function createFooter() {
    const footer = document.getElementById('footer');
    const footerContent = document.createElement('footer');
    footerContent.innerHTML = '<div class="line"></div><div class="grid-container-footer"><div class="titulos"><h3>Recursos</h3></div><div class="titulos"><h3>Redes Sociales</h3></div><div class="titulos"><h3>Volver al inicio</h3></div><div class="grid-items"><ul><li><a href="">Politica de privacidad</a></li><li><a href="">Informacion legal</a></li><li><a href="">Cookies</a></li></ul></div><div class="grid-img"><img class ="grid-icon" src="imagenes/facebook.png" alt="facebook"><img class ="grid-icon" src="imagenes/twitter.png" alt="twitter"><img class ="grid-icon" src="imagenes/youtube.png" alt="youtube"><img class ="grid-icon" src="imagenes/logotipo-de-xbox.png" alt="xbox"></div><div class="grid-ancla"><a href="#ancla"><img src="imagenes/flecha-arriba.png" alt="flecha"></a></div><div class="grid-text"><p>© 2023 FG Footer Games. Todos los derechos reservados. Todas las marcas registradas pertenecen a sus respectivos dueños en Argentina y otros países.</p></div></div><div class="line"></div';
    footer.appendChild(footerContent);
}

// Llama a las funciones para crear el header y el footer
createHeader();
createFooter();

