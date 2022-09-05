#!/usr/bin/node
/*
let gremlin = 1;
if (!isNaN(process.argv[2])) {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    gremlin *= i;
  }
}
console.log(gremlin);
*/
console.log(fac(parseInt(process.argv[2])));
function fac (n) {
  if (!n || n === 0 || n === 1) {
    return 1;
  } else {
    return n * fac(n - 1);
  }
}
