let pizzaIndex = 1; 
let repartidorIndex = 0; 

const pizzaImagenes = [
    "static/img/pizza1.webp",
    "static/img/pizza2.webp",
    "static/img/pizza3.webp",
    "static/img/pizza4.webp"
];

const pizzaSabores = [
    "Pepperoni",
    "Queso",
    "Hawaiana",
    "Mexicana"
];



// Función para cambiar las imágenes y el sabor de las pizzas
function cambiarImagenPizza(direccion) {
    pizzaIndex += direccion;

    if (pizzaIndex >= listaPizzas.length) pizzaIndex = 0;  // Volver al primer elemento
    if (pizzaIndex < 0) pizzaIndex = listaPizzas.length - 1;  // Volver al último elemento

    document.getElementById("pizzaImg").src = `static/img/${listaPizzas[pizzaIndex].imagen}`;

    document.getElementById("pizzaSabor").textContent = listaPizzas[pizzaIndex].nombre;
}

function cambiarImagenRepartidor(direccion) {
    repartidorIndex += direccion;
    
    // Asegurar que el índice sea válido
    if (repartidorIndex >= listaRepas.length) repartidorIndex = 0;  // Volver al inicio
    if (repartidorIndex < 0) repartidorIndex = listaRepas.length - 1;  // Volver al final

    // Cambiar la imagen del repartidor
    document.getElementById("repartidorImg").src = `static/img/${listaRepas[repartidorIndex].imagen}`;

    // Cambiar el nombre del repartidor
    document.getElementById("repartidorNombre").textContent = listaRepas[repartidorIndex].nombre;
}
