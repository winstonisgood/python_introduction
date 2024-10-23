a = [1,2,3]
b = 4

console.log("a in the first initial: " + a);
console.log("b in the first initial: " + b);

function add(a, b) {
    a.push(b)
    b = a;
    console.log("a in the function: " + a);
    console.log("b in the function: " + b);
}

add(a, b)
console.log("a after function: " + a);
console.log("b after function: " + b);