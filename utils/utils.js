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

const testPrimeSieve = () => {
  const knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
  const gen = primeSieve(30);
  for (let i = 0; i < knownPrimes.length; i++) {
    if (knownPrimes[i] !== gen.next().value) {
      console.log(`We fucked up at ${knownPrimes[i]}`);
    }
  }
}

testPrimeSieve();

const isPalindrome = num => {
  const s = String(num);
  for (let i = 0, j = s.length - 1; i <= s.length / 2; i++, j--) {
    if (s[i] !== s[j]) return false;
  }
  return true;
};


const testIsPalindrome = () => {
  const knownPalindromes = [101, 20002, 298374473892];
  knownPalindromes.forEach(palindrome => {
    if (!isPalindrome(palindrome)) {
      console.log(`We failed to identify ${palindrome} as a palindrome`);
    }
  });
};

testIsPalindrome();

module.exports = {
  primeSieve,
  isPalindrome,
};
