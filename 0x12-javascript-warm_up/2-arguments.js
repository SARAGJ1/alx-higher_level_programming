#!/usr/bin/node
if (process.argv[2] != null && process.argv[3] == null) {
  console.log('Argument found');
} else if (process.argv[2] != null && process.argv[3] != null) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
