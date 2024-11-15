const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const pointer = document.getElementById("pointer");
const scrollSpeed = 0.1;

let isPainting = false;
let isErasing = false;
let penSize = 10;
let penX = 0;
let penY = 0;

addEventListener("wheel", (e) => {
    penSize += e.deltaY * scrollSpeed;
    updatePointer();
});

addEventListener("mousemove", (e) => {
    penX = e.pageX;
    penY = e.pageY;
    updatePointer();
});

function updatePointer() {
    pointer.style.height = penSize + "px";
    pointer.style.left = penX - pointer.clientWidth / 2 + "px";
    pointer.style.top = penY - pointer.clientWidth / 2 + "px";
}

addEventListener("drag", (e) => {
    ctx;
});
