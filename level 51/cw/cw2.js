let score = Float(prompt("enter your score: "));

if (score >= 90 && score <= 100){
    console.log("შესანიშნავია, თქვენ გამოცდა დაწერეთ უმაღლეს დონეზე");
} else if (score >= 80 && score < 90) {
    console.log("გილოცავთ, თქვენ გამოცდა დაწერეთ კარგ დონეზე");
} else if (score >= 70 && score <80) {
    console.log("გილოცავთ, თქვენ გამოცდა დაწერეთ ნორმალურ დონეზე");
} else if (score >= 60 && score < 70){
    console.log( "გილოცავთ, თქვენ გამოცდა დაწერეთ ცუდ დონეზე")
} else{
    console.log("no score67")
}