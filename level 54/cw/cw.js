function division(a, b) {
    return a / b;
}

// ფუნქციის გამოძახება და შედეგის კონსოლში გამოტანა
console.log(division(10, 2)); // დაიბეჭდება: 5


function myAge(age) {
    return age;
}

function myAgeString(string1) {
    return `${string1} ${myAge(20)}`; // myAge გამოიყენება როგორც helper ფუნქცია
}

// შედეგის გამოტანა
console.log(myAgeString("my age is")); // დაიბეჭდება: my age is 20


const checkEducation = (age) => {
    if (age === 18) {
        return "შენ ჩააბარე უნივერსიტეტში";
    } else {
        return "ჯერ კიდევ სკოლაში ხარ";
    }
};

// შემოწმება მაგალითებით:
console.log(checkEducation(18)); // დაიბეჭდება: შენ ჩააბარე უნივერსიტეტში
console.log(checkEducation(15)); // დაიბეჭდება: ჯერ კიდევ სკოლაში ხარ