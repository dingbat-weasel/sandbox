sandbox/
└── sketches/
    ├── index.html        # open this in a browser to run the sketch
    ├── sketch.js         # all your drawing code lives here
    └── README.md         # optional: note what concept the sketch is exploring

────────────────────────────────────────────
index.html
────────────────────────────────────────────
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.9.0/lib/p5.min.js"></script>
  </head>
  <body>
    <script src="sketch.js"></script>
  </body>
</html>

────────────────────────────────────────────
sketch.js
────────────────────────────────────────────
function setup() {
  // runs once when the sketch starts
  // createCanvas(width, height) — sets the size of your drawing area in pixels
  createCanvas(800, 400);
}

function draw() {
  // runs continuously in a loop (like a game loop)
  // for static drawings you mostly just let it redraw the same thing
  background(255); // 255 = white, 0 = black

  // your drawing code goes here
}

────────────────────────────────────────────
folder structure note
────────────────────────────────────────────
// as sketches accumulate, give each concept its own folder:
//
// sketches/
// ├── 01-number-line/
// ├── 02-commutativity/
// ├── 03-distributive-property/
// └── ...
//
// keep each sketch self-contained — its own index.html + sketch.js
// the top-level sketches/index.html can just be a plain list of links