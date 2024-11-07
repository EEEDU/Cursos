"use strict";
// Constante de distintos tipos
const msg = "Hola mundo que tal";
// Diccionarios
const hero = {
    name: "Capitan",
    age: 30
};
// Imprimir por pantalla
console.log(hero.age + 1);
// Funciones
function sayHello(msg) {
    console.log(msg);
}
// Funcion autoejecutable
(() => {
    let isSuper = false;
    console.log(isSuper);
})();
// Array
const numbers = [1, 2, "3", 4, 5, 6, 7, 8];
numbers.push(1, 2, 3, 4, 5, 6, 7, "4");
const numbers2 = [1, 2, 3, 4, 5, 6, 7];
numbers2.forEach(number => console.log(number));
// Tuplas 
const tupla = ["hola", 43, true];
// Enumerables
(() => {
    let AudioLevel;
    (function (AudioLevel) {
        AudioLevel[AudioLevel["min"] = 1] = "min";
        AudioLevel[AudioLevel["medium"] = 2] = "medium";
        AudioLevel[AudioLevel["max"] = 10] = "max";
    })(AudioLevel || (AudioLevel = {}));
    const currentAudio = AudioLevel.medium;
    console.log(AudioLevel);
})();
// Never 
const abc = (message) => {
    throw new Error(message);
};
