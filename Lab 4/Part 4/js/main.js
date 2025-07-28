// set up canvas
const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

const width = (canvas.width = window.innerWidth);
const height = (canvas.height = window.innerHeight);

// function to generate random number
function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// function to generate random RGB color value
function randomRGB() {
  return `rgb(${random(0, 255)},${random(0, 255)},${random(0, 255)})`;
}

// Base Shape class for common properties (position, velocity)
class Shape {
  constructor(x, y, velX, velY) {
    this.x = x;
    this.y = y;
    this.velX = velX;
    this.velY = velY;
  }
}

// Ball class extends Shape with drawing, movement and collision logic
class Ball extends Shape {
  constructor(x, y, velX, velY, color, size) {
    /* adds color, size and existence flag */ 
    super(x, y, velX, velY);
    this.color = color;
    this.size = size;
    this.exists = true;
  }
 /* draws colored circle */
  draw() {
    ctx.beginPath();
    ctx.fillStyle = this.color;
    ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
    ctx.fill();
  }
 /* handles wall bouncing with velocity reversal */ 
  update() {
    if (this.x + this.size >= width) {
      this.velX = -Math.abs(this.velX);
    }

    if (this.x - this.size <= 0) {
      this.velX = Math.abs(this.velX);
    }

    if (this.y + this.size >= height) {
      this.velY = -Math.abs(this.velY);
    }

    if (this.y - this.size <= 0) {
      this.velY = Math.abs(this.velY);
    }

    this.x += this.velX;
    this.y += this.velY;
  }
/* detects ball collisions and changes colors */
  collisionDetect() {
    for (const ball of balls) {
      if (!(this === ball) && ball.exists) {
        const dx = this.x - ball.x;
        const dy = this.y - ball.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < this.size + ball.size) {
          ball.color = this.color = randomRGB(); // This changes both balls' colors
        }
      }
    }
  }

}
// EvilCircle class (player-controlled) with special behaviors
class EvilCircle extends Shape {
  constructor(x, y) {
     /* sets up keyboard controls via event listener */
    super(x, y, 20, 20);
    this.color = "white";
    this.size = 10;

    window.addEventListener("keydown", (e) => {
      switch (e.key) {
        case "a":
          this.x -= this.velX;
          break;
        case "d":
          this.x += this.velX;
          break;
        case "w":
          this.y -= this.velY;
          break;
        case "s":
          this.y += this.velY;
          break;
      }
    });
  }
 /* draws outlined circle */
  draw() {
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = this.color;
    ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
    ctx.stroke();
  }
/* prevents leaving canvas */ 
  checkBounds() {
    if (this.x + this.size >= width) {
      this.x -= this.size;
    }

    if (this.x - this.size <= 0) {
      this.x += this.size;
    }

    if (this.y + this.size >= height) {
      this.y -= this.size;
    }

    if (this.y - this.size <= 0) {
      this.y += this.size;
    }
  }
 /* "eats" balls on contact */
  collisionDetect() {
    for (const ball of balls) {
      if (ball.exists) {
        const dx = this.x - ball.x;
        const dy = this.y - ball.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < this.size + ball.size) {
          ball.exists = false;
        }
      }
    }
  }
}
// Create 25 random balls with varying properties
const balls = [];
while (balls.length < 25) {
  const size = random(10, 20);
  const ball = new Ball(
    random(0 + size, width - size),
    random(0 + size, height - size),
    random(-7, 7),
    random(-7, 7),
    randomRGB(),
    size
  );
/* random position/speed/color/size */
  balls.push(ball);
}
// Create player-controlled evil circle
const evilBall = new EvilCircle(random(0, width), random(0, height));
// Main animation loop
function loop() {
  // Clear canvas with semi-transparent black (
  ctx.fillStyle = "rgba(0, 0, 0, 0.25)";
  ctx.fillRect(0, 0, width, height);
 // Update and draw all active balls
  for (const ball of balls) {
    if (ball.exists) {
      ball.draw();
      ball.update();
      ball.collisionDetect();
    }
  }
  // Handle evil circle operations
  evilBall.draw();
  evilBall.checkBounds();
  evilBall.collisionDetect();

  // Update ball count display
  document.querySelector('p').textContent = `Balls remaining: ${balls.filter(b => b.exists).length}`;
// Continue animation
  requestAnimationFrame(loop);
}
// Start animation
loop();