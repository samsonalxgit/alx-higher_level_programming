#!/usr/bin/node
const process = require('process');
let resp;
if (process.argv.length === 1) {
  resp = 'Argument found';
} else if (process.argv.length < 1) {
  resp = 'No argument';
} else {
  resp = 'Arguments found';
}
console.log(resp);
