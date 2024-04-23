#!/usr/bin/node
function factorial (n) {
  let fac = 1;
  while (n !== 0) {
    fac = fac * n;
    n = n - 1;
  }
  return (fac);
}
if (process.argv[2] !== undefined) {
  console.log(factorial(Number(process.argv[2])));
} else {
  console.log('1');
}
