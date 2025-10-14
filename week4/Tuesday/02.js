function joinArraysById(arr1, arr2) {
  const map = new Map();

  // Add all objects from arr1
  for (const obj of arr1) {
    map.set(obj.id, { ...obj });
  }

  // Merge or add objects from arr2
  for (const obj of arr2) {
    if (map.has(obj.id)) {
      // Merge: arr2 overrides arr1
      const merged = { ...map.get(obj.id), ...obj };
      map.set(obj.id, merged);
    } else {
      map.set(obj.id, { ...obj });
    }
  }

  // Convert map values to array and sort by id
  return Array.from(map.values()).sort((a, b) => a.id - b.id);
}


const arr1 = [
  { id: 1, x: 2, y: 3 },
  { id: 2, x: 3, y: 6 }
];

const arr2 = [
  { id: 2, x: 10, y: 20 },
  { id: 3, x: 0, y: 0 }
];

console.log(joinArraysById(arr1, arr2));



