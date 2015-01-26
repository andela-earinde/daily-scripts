function fibonacci (n) {
    // Count the number of calls
    if (!this.count) {
        this.count = 1;
    } else {
        this.count += 1;
        console.log("Called " + this.count + " times.");
    }

    if (!this.processed) {
        this.processed = [];
    }

    if (n <= 1) {
        this.processed[n] = 1
        return this.processed[n];
    } else {
        if (!this.processed[n]) {
            this.processed[n] = fibonacci(n - 1) + fibonacci(n - 2);
        }

        return this.processed[n];
    }
}

var number = +(process.argv[2]);
console.log(fibonacci(number));
