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

  let a = 500;
  let b = 250;
  let c = 250;

  offset = 50;

  rect(offset, offset, b + c, a);
  line(b + offset, offset, c + offset, a + offset);
}
