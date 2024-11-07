(() => {
    const fullName = ( firsName: string, ...restArgs: string[]): string => {
        return `${firsName} ${restArgs.join('')}`;  
    }

    const superman = fullName ('Clark', 'superman');


})()