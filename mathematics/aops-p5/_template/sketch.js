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

function draw() {
  translate(0, height);
  scale(1, -1);
}
