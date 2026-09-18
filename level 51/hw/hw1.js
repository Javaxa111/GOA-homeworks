let temp = parseFloat(prompt("sheiyvanet temperatura:"));

if (temp < 0) {
    console.log("Cold ❄️");
} else if (temp <= 30) {
    console.log("Normal 🌤️");
} else {
    console.log("Hot ☀️");
}