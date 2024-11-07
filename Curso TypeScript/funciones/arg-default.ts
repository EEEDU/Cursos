(() => {
    const fullName = ( firstName: string, lastName?: (string | boolean) , upper: boolean = false): string => {
        return `${firstName} ${lastName || "-----"}`;
    }

    const name = fullName( "Eduardo", true)
    const name2 = fullName( "Eduardo", false, true)
})()