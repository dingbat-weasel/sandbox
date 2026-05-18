function setup() {
  createCanvas(800, 800);
  background('lightblue');
}

function fx(x) {
  return x;
}
function fy(y) {
  return height - y;
}

const offset = 50;
let a = 500;
let b = 250;
let c = 250;

class HandleWidth {
  constructor(orgX, orgY, wid, hei) {
    this.dragging = false;
    this.rollover = false;

    this.x = orgX;
    this.y = orgY;

    this.w = wid;
    this.h = hei;
  }

  over() {
    // is mouse over object
    if (
      mouseX > this.x &&
      mouseX < this.x + this.w &&
      mouseY > this.y &&
      mouseY < this.y + this.h
    ) {
      this.rollover = true;
    } else {
      this.rollover = false;
    }
  }

  update() {
    // adjust size if dragged
    if (this.dragging) {
    }
  }
}

function drag_width() {}

function draw() {
  translate(0, height);
  scale(1, -1);

  // a*b
  rect(offset, offset, b, a);
  // a*c
  rect(b + offset, offset, c, a);

  let total_width = b + c;

  // handle for width
  rect(offset + b + c - 5, a * 0.25 + offset, 10, a * 0.5, 5, 5, 5, 5);

  // handle for height
  rect(
    total_width * 0.25 + offset,
    offset + a - 5,
    total_width * 0.5,
    10,
    5,
    5,
    5,
    5,
  );

  // slider
  circle(offset + b, offset, 25);
}
