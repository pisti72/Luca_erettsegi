let cloud1 = document.getElementById("cloud1");
let cloud2 = document.getElementById("cloud2");
let clouds = [cloud1, cloud2];
let cloudsX = [100, 700];
let cloudsY = [10, 50];
function update() {
    for (let i = 0; i < clouds.length; i++) {
        clouds[i].style.left = cloudsX[i] + "px";
        clouds[i].style.top = cloudsY[i] + "px";
        cloudsX[i] -= 1;
        if (cloudsX[i] < -clouds[i].width) {
            cloudsX[i] = window.innerWidth;
        }
    }

    requestAnimationFrame(update);
}
update();