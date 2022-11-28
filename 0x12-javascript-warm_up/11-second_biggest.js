#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv;
  console.log(list.sort((a, b) => a - b).slice(5)[1]);
}
