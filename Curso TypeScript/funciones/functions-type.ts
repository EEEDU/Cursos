(() => {
    // const addNumbers = (a: number, b:number): number => {
    //     return a + b;
    // }
    const addNumbers = (a: number, b: number): number => a + b;
    const saludar = (name: string): string => "Hola ${name}"; 
    const saveTheWorld = (): string => "ok";

    let myFunction;

    myFunction = addNumbers; 

    myFunction(1,3);
})()
