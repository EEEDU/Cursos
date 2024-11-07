"use strict";
(() => {
    const fullName = (firsName, ...restArgs) => {
        return `${firsName} ${restArgs.join('')}`;
    };
    const superman = fullName('Clark', 'superman');
})();
