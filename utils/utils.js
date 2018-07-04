function* primeSieve(max) {
  const sieve = new Array(max - 2);
  let currentNumber = 2;
  while (currentNumber <= max) {
    yield currentNumber;
    for (let i = currentNumber; i <= max; i+=currentNumber) {
      sieve[i - 2] = true;
    }

    for (; sieve[currentNumber - 2]; currentNumber++) {}
  }
}

const test = () => {
  const knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
  const gen = primeSieve(30);
  for (let i = 0; i < knownPrimes.length; i++) {
    if (knownPrimes[i] !== gen.next().value) {
      console.log(`We fucked up at ${knownPrimes[i]}`);
    }
  }
}

test();

module.exports = {
  primeSieve,
};
