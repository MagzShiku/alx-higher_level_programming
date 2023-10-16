#!/usr/bin/node
// searches the second biggest integer in the list of arguments

const ints = process.argv.slice(2);

if (ints.length <= 1) {
  console.log(0);
} else {
  const sortedInts = ints.map(Number).sort((a, b) => b - a);
  console.log(sortedInts[1]);
}
