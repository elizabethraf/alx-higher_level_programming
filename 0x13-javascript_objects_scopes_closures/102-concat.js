#!/usr/bin/node
const fileSystem = require('fs');
const firstarg = fileSytem.readFileSync(process.argv[2]).toString();
const fileSystem = fileSystem.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], (firstarg + secondarg));
