#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    return (number.toString(base));
  };
};
