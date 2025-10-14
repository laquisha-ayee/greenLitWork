function memoize(fn) {
  const cache = new Map();
  let callCount = 0;

  return {
    
    call: (...args) => {
      const key = JSON.stringify(args);

      if (cache.has(key)) {
        return cache.get(key);
      }

      const result = fn(...args);
      cache.set(key, result);
      callCount++;
      return result;
    },

    getCallCount: () => {
      return callCount;
    }
  };
}



// Example 1: sum
const sum = (a, b) => a + b;
const memoSum = memoize(sum);
console.log(memoSum.call(2, 2)); 
console.log(memoSum.call(2, 2)); 
console.log(memoSum.getCallCount()); 
console.log(memoSum.call(1, 2)); 
console.log(memoSum.getCallCount()); 

// Example 2: factorial
const factorial = (n) => n <= 1 ? 1 : n * factorial(n - 1);
const memoFactorial = memoize(factorial);
console.log(memoFactorial.call(3)); 
console.log(memoFactorial.call(3)); 
console.log(memoFactorial.getCallCount()); 

// Example 3: fib
const fib = (n) => n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
const memoFib = memoize(fib);
console.log(memoFib.call(5)); 
console.log(memoFib.getCallCount()); 



