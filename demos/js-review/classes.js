// Slides 283-286: classes
// Run: node classes.js

class Shape {
  constructor(id, x, y) {
    this.id = id;
    this.x = x;
    this.y = y;
  }
  describe() {
    return `${this.constructor.name} ${this.id} at (${this.x}, ${this.y})`;
  }
}

class Rectangle extends Shape {
  constructor(id, x, y, width, height) {
    super(id, x, y); // must come before using `this`
    this.width = width;
    this.height = height;
  }
  get area() {
    return this.width * this.height;
  }
}

class Circle extends Shape {
  #radius; // private field (ES2022)
  constructor(id, x, y, radius) {
    super(id, x, y);
    this.#radius = radius;
  }
  get area() {
    return Math.round(Math.PI * this.#radius ** 2);
  }
}

for (const s of [new Rectangle('r1', 0, 0, 3, 4), new Circle('c1', 5, 5, 2)]) {
  console.log(s.describe(), 'area:', s.area);
}

// A named class expression: the inner name is only visible inside the class
const Square = class Rect {
  whoAmI() {
    return Rect.name;
  }
};
console.log(new Square().whoAmI(), typeof Rect); // 'Rect' 'undefined'
