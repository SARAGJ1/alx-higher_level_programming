#!/usr/bin/node
if (process.argv[2] === undefined || (Number(process.argv[2]) === 1 && process.argv[3] === undefined)) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
