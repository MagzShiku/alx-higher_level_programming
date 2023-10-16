#!/usr/bin/node
// script that computes and prints a factorial

function myFactorial (i) {
  if (isNaN(i)) {
    return 1;
  }
  if (i === 0) {
    return 1;
  }
  return i * myFactorial(i - 1);
}

const arg = process.argv[2];
const myNum = parseInt(arg);

console.log(myFactorial(myNum));
