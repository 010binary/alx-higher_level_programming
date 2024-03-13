#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const files = require('fs');
const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');
files.writeFileSync(fileC, textA + textB);
