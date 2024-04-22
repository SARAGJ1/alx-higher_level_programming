#!/usr/bin/node
if (process.argv[2] == null) {
  console.log('No argument');
} else {
  const args = process.argv.slice(2);
  let i = 0, result = '';
  while (args[i] != null) {
    result += args[i] + ' ';
    i = i + 1;
  }
  console.log(result.trim());
}
