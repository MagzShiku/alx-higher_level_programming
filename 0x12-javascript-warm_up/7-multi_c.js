#!/usr/bin/node
// prints x times “C is fun”

const myArg = process.argv[2];
const myTimes = parseInt(myArg);

if (isNaN(myTimes)) {
  console.log('Missing number of occurrences');
} else if (myTimes < 0) {
  // do nothing
} else {
  for (let i = 0; i < myTimes; i++) {
    console.log('C is fun');
  }
}
