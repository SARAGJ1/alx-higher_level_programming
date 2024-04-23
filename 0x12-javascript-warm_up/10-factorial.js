#!/usr/bin/node
function factorial (n) {
  let fac = 1;
  if (n !== undefined) {
    while (n !== 0) {
      fac = fac * n;
      n = n - 1;
    }
  return (fac);
  } else {
  return (1);
  }
}
console.log(factorial(Number(process.argv[2])));
