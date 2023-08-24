const leapYear = function (num) {
    let isLeapYear = false;

    if (typeof num !== "number") {
        console.log("What the hell are you doing?")
        return null;
    } else if (num % 400 === 0) {
        isLeapYear = true;
    } else if (num % 100 === 0) {
        isLeapYear = false;
    } else if (num % 4 === 0) {
        isLeapYear = true;
    }

    return isLeapYear;
}

module.exports = leapYear;