#!/usr/bin/node
if (process.argv[2] != null) {
  let num = 0;
  num = Number(process.argv[2]);
  if (Number.isInteger(num)) {
    console.log('My number: %d', num);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
