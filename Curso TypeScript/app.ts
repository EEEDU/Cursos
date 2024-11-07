// Constante de distintos tipos
const msg: string = "Hola mundo que tal";

// Diccionarios
const hero = {
    name: "Capitan",
    age: 30
}

// Imprimir por pantalla
console.log(hero.age + 1);

// Funciones
function sayHello (msg: string) {
    console.log(msg);
}

// Funcion autoejecutable
(() => {
    let isSuper = false;

    console.log(isSuper)
})()

// Array
const numbers = [1, 2, "3", 4, 5, 6, 7, 8];
numbers.push(1, 2, 3, 4, 5, 6, 7,"4");

const numbers2: number[] = [1, 2, 3, 4, 5, 6, 7]; 
numbers2.forEach(number => console.log(number));

// Tuplas 
const tupla: [string, number, boolean] = ["hola", 43, true];

// Enumerables
(() => {
    enum AudioLevel {
        min = 1,
        medium,
        max = 10
    }

    const currentAudio = AudioLevel.medium;

    console.log(AudioLevel);
})()

// Never 
const abc = ( message: string):never => {
    throw new Error(message);
}