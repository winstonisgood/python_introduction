function pickNumbers(poolSize, ballNum) {
    // Create and fill numbers array
    const numbers = [];
    for (let i = 1; i <= poolSize; i++) {
        numbers.push(i);
    }
    
    // Random index and shuffle numbers (Fisher-Yates algorithm)
    for (let i = numbers.length - 1; i > 0; i--) {
        // Pick random index from 0 to i inclusive
        const j = Math.floor(Math.random() * (i + 1));
        // Swap numbers[i] and numbers[j] (at random index)
        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
    }
    
    // Initialize the winning numbers array
    const winningNumbers = [];
    // Set conditions to pop the numbers from the array and push to the winningNumbers array
    while (winningNumbers.length < ballNum) {
        winningNumbers.push(numbers.pop());
    }
    
    return winningNumbers;
}

// Test the function
const winningSeven = pickNumbers(35, 7);
const pBall = pickNumbers(20, 1);

console.log(`The winning seven numbers are: ${winningSeven}`);
console.log(`The P ball is ${pBall}`);