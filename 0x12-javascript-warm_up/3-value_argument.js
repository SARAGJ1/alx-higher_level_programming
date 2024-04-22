#!/usr/bin/node
if (process.argv[2] == null) {
  console.log('No argument');
} else {
  const args = process.argv.slice(2);
  let i = 0;
  while (args[i] != null) {
    console.log(args[i]);
    i = i + 1;
  }
}
