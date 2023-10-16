#!/usr/bin/node
// prints My number: <first argument converted in integer>
// if the first argument can be converted to an intege
// If the argument can’t be converted to an integer, print “Not a number”

const myArg = process.argv[2];
const myNum = parseInt(myArg);

if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + myNum);
}
