const primeSieve = require('../../utils/utils').primeSieve;

const p003 = (num=600851475143) => {
  const gen = primeSieve(Math.ceil(Math.sqrt(num)));
  let maxPrime = 0;
  for (let nextVal = gen.next(); !nextVal.done; nextVal = gen.next()) {
    const value = nextVal.value;
    if (num % value === 0 && value > maxPrime) {
      maxPrime = value;
    }
  }

  return maxPrime;
};

console.log(p003()); // 6857
