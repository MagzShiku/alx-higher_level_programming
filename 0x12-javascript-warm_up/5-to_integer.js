#!/usr/bin/node
// prints My number: <first argument converted in integer>

const myArg = process.argv[2];
const myNum = parseInt(myArg);

if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
