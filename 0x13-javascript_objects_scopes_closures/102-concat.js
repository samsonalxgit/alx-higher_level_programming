#!/usr/bin/node

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
const fs = require('fs');
const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, textA + textB);
