function setup() {
  createCanvas(800, 800);
  background('lightblue');
}

function mx(x) {
  return x;
}
function my(y) {
  return height - y;
}

function draw() {
  translate(0, height);
  scale(1, -1);
}
