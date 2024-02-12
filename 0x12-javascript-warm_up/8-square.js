#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
    let i = 0;
    while (i < x) {
	console.log('X'.repeat(x));
	i++;
    }
}
