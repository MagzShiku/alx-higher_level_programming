#!/usr/bin/node
// Script that ads two integers

function add (a, b) {
  return a + b;
}
const val1 = process.argv[2];
const val2 = process.argv[3];

const num1 = parseInt(val1);
const num2 = parseInt(val2);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
