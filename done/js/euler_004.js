const isPalindrome = require('../../utils/utils').isPalindrome;

const p004 = (min = 900) => {
  for (let i = 999; i > min; i--) {
    for (let j = 999; j > min; j--) {
      const num = i * j;
      if (isPalindrome(num)) {
        return num;
      }
    }
  }
  return -Infinity;
};

console.log(p004());
