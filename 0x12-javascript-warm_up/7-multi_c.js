#!/usr/bin/node
let i = 0;
if (Number.isInteger(Number(process.argv[2]))) {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i += 1;
  }
} else {
  console.log('Missing number of occurrences');
}
