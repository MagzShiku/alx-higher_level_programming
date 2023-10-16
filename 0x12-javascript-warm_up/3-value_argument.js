#!/usr/bin/node
// prints the first argument passed to it:

const myArg = process.argv[2];

if (!myArg) {
  console.log('No argument');
} else {
  console.log(myArg);
}
