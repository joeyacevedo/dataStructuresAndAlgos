var createHelloWorld = function () {
  return function () {
    return 'Hello World';
  };
};

createHelloWorld();

var createCounter = function (n) {
  let iterator = 0;

  return function () {
    let answer = n + iterator;
    iterator++;
    return answer;
  };
};

createCounter(1);
