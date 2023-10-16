#!/usr/bin/node
// a script that prints a square

const myArg = process.argv[2];
const mySquare = parseInt(myArg);

if (isNaN(mySquare) || mySquare <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < mySquare; i++) {
    let row = '';
    for (let j = 0; j < mySquare; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
