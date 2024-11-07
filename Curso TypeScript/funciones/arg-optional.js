"use strict";
(() => {
    const fullName = (firstName, lastName) => {
        return `${firstName} ${lastName || "-----"}`;
    };
    const name = fullName("Eduardo", true);
    const name2 = fullName("Eduardo");
})();
