// setup canvas

const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

const width = (canvas.width = window.innerWidth);
const height = (canvas.height = window.innerHeight);

// function to generate random number

function random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// function to generate random color

function randomRGB() {
  return `rgb(${random(0, 255)},${random(0, 255)},${random(0, 255)})`;
}


// Ball class to represent each bouncing ball
class Ball {
  constructor(x, y, velX, velY, color, size) {
    this.x = x;
    this.y = y;
    this.velX = velX;
    this.velY = velY;
    this.color = color;
    this.size = size;
  }

    // Draw the ball on the canvas
  draw() {
    ctx.beginPath();
    ctx.fillStyle = this.color;
    ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
    ctx.fill();
    }

  // Update ball position and handle wall collisions
    update() {
         // Reverse velocity if ball hits right/left walls
    if (this.x + this.size >= width) {
      this.velX = -this.velX;
    }

    if (this.x - this.size <= 0) {
      this.velX = -this.velX;
    }
    // Reverse velocity if ball hits top/bottom walls
    if (this.y + this.size >= height) {
      this.velY = -this.velY;
    }

    if (this.y - this.size <= 0) {
      this.velY = -this.velY;
    }

        // Update position based on velocity
    this.x += this.velX;
    this.y += this.velY;
  }
    // Detect collisions with other balls and change colors on impact
    collisionDetect() {
    for (const ball of balls) {
      if (this !== ball) {
        const dx = this.x - ball.x;
        const dy = this.y - ball.y;
        const distance = Math.sqrt(dx * dx + dy * dy);
    
        // If balls collide, change both colors
        if (distance < this.size + ball.size) {
          ball.color = this.color = randomRGB();
        }
      }
    }
  }
}

// Creates a test ball at position with velocity
const testBall = new Ball(50, 100, 4, 4, "blue", 10);
testBall.x;
testBall.size;
testBall.color;
testBall.draw();

// Create an array to store all balls
const balls = [];

// Generate 25 random balls
while (balls.length < 25) {
  const size = random(10, 20);
  const ball = new Ball(
    // ball position always drawn at least one ball width
    // away from the edge of the canvas, to avoid drawing errors
    random(0 + size, width - size),
    random(0 + size, height - size),
    random(-7, 7),
    random(-7, 7),
    randomRGB(),
    size,
  );

  balls.push(ball);
}

// Main animation loop

function loop() {
    // Clear canvas with semi-transparent black (creates motion trail effect)
  ctx.fillStyle = "rgb(0 0 0 / 25%)";
  ctx.fillRect(0, 0, width, height);

    // Update and draw each ball
  for (const ball of balls) {
    ball.draw();
    ball.update();
    ball.collisionDetect();
  }
  // Continue the animation loop

  requestAnimationFrame(loop);
}
// Start the animation
loop();