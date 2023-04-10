#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length;
  let index = 0;
  const newArray = [];
  while (index < len) {
    newArray[index] = list[len - 1];
    newArray[len - 1] = list[index];
    index++;
    len--;
  }
  return (newArray);
};
