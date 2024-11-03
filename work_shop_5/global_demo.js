var x = 0;

function increment() {
    x = 20;
    console.log(x, 'inside increment');
    return;
}

increment();
console.log(x, 'outside increment');