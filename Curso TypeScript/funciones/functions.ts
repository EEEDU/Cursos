(() => {
    const hero: string = "flash";

    function returnName (): string {
        return hero;
    }
   
    const activateBatisignal = (): string => {
        return "batisignal";
    }

    console.log( typeof activateBatisignal );
})()