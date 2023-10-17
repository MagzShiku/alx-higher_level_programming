#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data');
const userOcs = {};
for (const userId in dict) {
  const OOcs = dict[userId];
  if (OOcs in userOcs) {
    userOcs[OOcs].push(userId);
  } else {
    userOcs[OOcs] = [userId];
  }
}

console.log(userOcs);
