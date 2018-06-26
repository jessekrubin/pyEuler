// -*- coding: utf-8 -*-
// Jesse Rubin ~ Project Euler

// Multiples of 3 and 5
// Problem 1
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we
// get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.
// p001 = (upper_bound = 1000) => {
//     return Array.from(Array(upper_bound).keys())
//         .filter(value => value % 3 === 0 || value % 5 === 0)
// .reduce(function(acc, val) {
//         return acc + val;
//     });
// };
const p001 = (upper_bound = 1000) => {

  return Array.from(Array(upper_bound).keys())
    .filter(value => value % 3 === 0 || value % 5 === 0)
    .reduce(function(acc, val) {
      return acc + val;
    });
};

const p001_2 = (upper_bound = 1000) => [...Array(upper_bound).keys()].map(num =>
        num % 5 === 0 || num % 3 === 0 ?
            num :
            null
    ).filter(s => s)
    .reduce((acc, num) => acc + num, 0);

console.log(p001_2());

console.log(p001());
