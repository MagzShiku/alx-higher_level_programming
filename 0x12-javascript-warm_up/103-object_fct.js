#!/usr/bin/node

// Update this script by adding a new function incr that increments the integer value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// my code
myObject.incr = function () {
  this.value++;
};
// end of my code
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
