function division(a, b) {
 
  if (b === 0) {
    console.log("ნულზე გაყოფა შეუძლებელია!");
    return;
  }
 
  console.log(a / b);
}


division(10, 2);
division(15, 3); 
division(8, 0); 