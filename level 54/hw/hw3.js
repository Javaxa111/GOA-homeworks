const sum = function(a, b) {
    return a + b;
};

const isEven = function(num) {
    return num % 2 === 0;
};

const checkSumParity = function(num1, num2) {
    let resultSum = sum(num1, num2);
 
    if (isEven(resultSum)) {
        return `${resultSum} — ლუწია.`;
    } else {
        return `${resultSum} — კენტია.`;
    }
};
