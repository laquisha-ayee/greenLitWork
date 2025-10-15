// Your solution
var isEmpty = function(obj) {
  if (Array.isArray(obj)) {
    return obj.length === 0;
  }
  return Object.keys(obj).length === 0;
};

// Provided test cases
const tests = [
  { input: {"x": 5, "y": 42}, expected: false },
  { input: {}, expected: true },
  { input: [null, false, 0], expected: false },
];

// Run tests
tests.forEach((test, index) => {
  const result = isEmpty(test.input);
  const passed = result === test.expected;
  console.log(`Test ${index + 1}:`, passed ? "Passed" : "Failed");
  if (!passed) {
    console.log("  Input:", test.input);
    console.log("  Expected:", test.expected);
    console.log("  Got:", result);
  }
});