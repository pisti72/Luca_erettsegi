const GRAVITY = 0.2
const JUMP_FORCE = 10
const PIPE_SPEED = 4
const PIPE_MIN = window.innerHeight / 5
const PIPE_RANGE = window.innerHeight / 2
const PIPE_GAP = window.innerHeight / 4
let cloud1 = document.getElementById("cloud1");
let cloud2 = document.getElementById("cloud2");
let clouds = [cloud1, cloud2];
let cloudsX = [100, 700];
let cloudsY = [10, 50];
let pipes = [
    {
        img: document.getElementById("pipe_bottom"),
        x: 600,
        y: 400
    }
]
let bird = {
    img: document.getElementById("bird"),
    x: 50,
    y: 50,
    yv: 0,
    update: function () {
        this.yv += GRAVITY
        this.y += this.yv
        this.img.style.left = this.x + "px"
        this.img.style.top = this.y + "px"
    },
    jump: function () {
        if (this.yv > 0) {
            this.yv = -JUMP_FORCE
        }
    }
}
function pipeUpdate() {
    for (let i = 0; i < pipes.length; i++) {
        let pipe = pipes[i]
        pipe.x -= PIPE_SPEED
        if (pipe.x < -pipe.img.width) {
            pipe.x = window.innerWidth
            pipe.y = window.innerHeight - PIPE_MIN - Math.floor(Math.random() * PIPE_RANGE)
        }
        pipe.img.style.left = pipe.x + "px"
        pipe.img.style.top = pipe.y + "px"
    }
}
document.addEventListener("keydown", function (e) {
    if (e.key == " ") {
        bird.jump()
    }

})
function update() {
    for (let i = 0; i < clouds.length; i++) {
        clouds[i].style.left = cloudsX[i] + "px";
        clouds[i].style.top = cloudsY[i] + "px";
        cloudsX[i] -= 1;
        if (cloudsX[i] < -clouds[i].width) {
            cloudsX[i] = window.innerWidth;
        }
    }
    bird.update()
    pipeUpdate()

    requestAnimationFrame(update);
}
update();