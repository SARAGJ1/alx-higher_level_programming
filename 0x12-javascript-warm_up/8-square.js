#!/usr/bin/node
let i = 0;
let k = Number(process.argv[2]);
if (Number.isInteger(k)) {
  let result = '';
  while (i < k) {
    result += 'x';
    i = i + 1;
  }
  for (i = 0; i < k; i++) {
    console.log(result);
  }
} else {
  console.log('Missing size');
}
