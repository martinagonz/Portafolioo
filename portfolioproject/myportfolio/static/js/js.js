




let app = document.getElementById('typewriter');
 
    let typewriter = new Typewriter(app, {
      loop: true,
      delay: 75,
    });
     
    typewriter
      .pauseFor(2500)
      .typeString('Estudiante de Informatica')
      .pauseFor(200)
      .deleteChars(10)
      .start();
      
let menuVisible = false;
//Función que oculta o muestra el menu
function mostrarOcultarMenu(){
    if(menuVisible){
        document.getElementById("nav").classList ="";
        menuVisible = false;
    }else{
        document.getElementById("nav").classList ="responsive";
        menuVisible = true;
    }
}

function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("nav").classList = "";
    menuVisible = false;
}
// Función que aplica las animaciones de las habilidades
function efectoHabilidades() {
    var skills = document.getElementById("skills");
    var distancia_skills = window.innerHeight - skills.getBoundingClientRect().top;
    if (distancia_skills >= 300) {
        let habilidades = document.getElementsByClassName("progreso");
        habilidades[0].classList.add("javascript");
        habilidades[1].classList.add("htmlcss");
        habilidades[2].classList.add("python");
        habilidades[3].classList.add("ingles");
        habilidades[4].classList.add("empatia");
        habilidades[5].classList.add("creatividad");
        habilidades[6].classList.add("colaboracion");
        habilidades[7].classList.add("manejo");
        
        // Añadir estrella después de la animación
        for (let i = 0; i < habilidades.length; i++) {
            habilidades[i].addEventListener("animationend", function() {
                addStarAfterAnimation(habilidades[i]);
            });
        }
    }
}

// Función para agregar una estrella después de la animación
function addStarAfterAnimation(element) {
    var star = document.createElement("span");
    star.innerHTML = "★"; // Aquí puedes ajustar el contenido de la estrella según tu preferencia
    star.classList.add("star"); // Aplica estilos CSS necesarios
    element.appendChild(star);
}



// Detectar el desplazamiento para aplicar la animación de la barra de habilidades
window.onscroll = function() {
    efectoHabilidades();
}



