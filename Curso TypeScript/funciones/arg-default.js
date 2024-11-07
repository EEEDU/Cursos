"use strict";
(() => {
    const fullName = (firstName, lastName, upper = false) => {
        return `${firstName} ${lastName || "-----"}`;
    };
    const name = fullName("Eduardo", true);
    const name2 = fullName("Eduardo", false, true);
})();
