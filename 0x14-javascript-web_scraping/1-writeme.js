#!/usr/bin/node
const fs = require('fs');

// Check if file path and string to write are provided
if (process.argv.length < 4) {
  console.error('Please provide both the file path and the string to write as arguments.');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`String "${stringToWrite}" has been successfully written to ${filePath}`);
  }
});
