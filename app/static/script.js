let pizzaIndex = 1; 
let repartidorIndex = 1; 

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

const repartidorImagenes = [
    "static/img/repa1.png",
    "static/img/repa2.png",
    "static/img/repa3.png"
];

const repartidorNombres = [
    "Margarito",
    "Oscar",
    "Vlad"
];

// Función para cambiar las imágenes y el sabor de las pizzas
function cambiarImagenPizza(direccion) {
    pizzaIndex += direccion;
    if (pizzaIndex >= pizzaImagenes.length) pizzaIndex = 0;  // Volver al primer elemento
    if (pizzaIndex < 0) pizzaIndex = pizzaImagenes.length - 1;  // Volver al último elemento
    document.getElementById("pizzaImg").src = pizzaImagenes[pizzaIndex];
    document.getElementById("pizzaSabor").textContent = pizzaSabores[pizzaIndex];
}

// Función para cambiar las imágenes y el nombre del repartidor
function cambiarImagenRepartidor(direccion) {
    repartidorIndex += direccion;
    if (repartidorIndex >= repartidorImagenes.length) repartidorIndex = 0;  // Volver al primer elemento
    if (repartidorIndex < 0) repartidorIndex = repartidorImagenes.length - 1;  // Volver al último elemento
    document.getElementById("repartidorImg").src = repartidorImagenes[repartidorIndex];
    document.getElementById("repartidorNombre").textContent = repartidorNombres[repartidorIndex];
}
