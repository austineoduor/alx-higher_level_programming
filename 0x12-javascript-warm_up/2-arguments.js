#!/usr/bin/node
// let many = ''
// let one = ''
// let nobody = ''
if (process.argv[3]) {
  console.log('Arguments found');
  // many = 'Arguments found'
} else if (process.argv[2]) {
  console.log('Argument found');
  // one = 'Argument found'
} else {
  console.log('No argument');
  // nobody = 'No argument'
}

// console.log(many ? many: (one ? one : (nobody ? nobody : 'catlolol')))
