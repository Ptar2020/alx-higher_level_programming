#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop

const langs = ['C is fun', 'Python is cool', 'Javascript is amazing'];

let i = 0;

while (i < 3) {
  console.log(langs[i]);
  i = i + 1;
}
