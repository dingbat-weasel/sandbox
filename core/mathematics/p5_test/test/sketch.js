function setup() {
  createCanvas(800, 800, WEBGL);
  walker = new Walker();
}

function draw() {
  background('orange');
  orbitControl();
  debugMode();
  walker.step();
  walker.show();
}

class Walker {
  constructor() {
    this.tx = 0;
    this.ty = 10000;
    this.tz = 20000;

    this.history = [];
  }

  step() {
    // let x = map(noise(this.tx), 0, 1, -width / 2, width / 2);
    // let y = map(noise(this.ty), 0, 1, -height / 2, height / 2);
    // let z = map(noise(this.tz), 0, 1, -400, 400);

    let x = mouseX - width / 2;
    let y = mouseY - height / 2;
    let z = map(noise(this.tz), 0, 1, -400, 400);

    this.tx += 0.0025;
    this.ty += 0.0025;
    this.tz += 0.0025;

    this.history.push(createVector(x, y, z));
    if (this.history.length > 500) {
      this.history.shift();
    }
  }

  show() {
    noFill();
    strokeWeight(2);
    // fill('red');
    stroke('red');

    beginShape();
    for (let pos of this.history) {
      vertex(pos.x, pos.y, pos.z);
    }
    endShape();

    let head = this.history[this.history.length - 1];
    if (head) {
      push();
      translate(head.x, head.y, head.z);
      stroke('red');
      fill('lightblue');
      box(50);
      pop();
    }
  }
}
