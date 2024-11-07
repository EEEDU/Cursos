(() => {
    const fullName = ( firstName: string, lastName?: (string | boolean) ): string => {
        return `${firstName} ${lastName || "-----"}`;
    }

    const name = fullName( "Eduardo", true)
    const name2 = fullName( "Eduardo")
})()