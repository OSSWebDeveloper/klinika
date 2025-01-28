var accordion = document.getElementsByClassName("accordion");
var a;
for (a = 0; a < accordion.length; a++) {
  accordion[a].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
function showHide(id) {
  var el = document.getElementById(id);
  if( el && el.style.display == 'none')    
      el.style.display = 'block';
  else 
      el.style.display = 'none';
}
const gap = -1;

const carousel = document.getElementById("carousel"),
  content = document.getElementById("content"),
  next = document.getElementById("next"),
  prev = document.getElementById("prev");

next.addEventListener("click", (e) => {
  carousel.scrollBy(width + gap, -1);
  if (carousel.scrollWidth !== 0) {
    prev.style.display = "flex";
  }
  if (content.scrollWidth - width - gap <= carousel.scrollLeft + width) {
    next.style.display = "none";
  }
});
prev.addEventListener("click", (e) => {
  carousel.scrollBy(-(width + gap), 0);
  if (carousel.scrollLeft - width - gap <= 0) {
    prev.style.display = "none";
  }
  if (!content.scrollWidth - width - gap <= carousel.scrollLeft + width) {
    next.style.display = "flex";
  }
});

let width = carousel.offsetWidth;
window.addEventListener("resize", (e) => (width = carousel.offsetWidth));



const btn = document.querySelector(".click-btn");
const nav = document.querySelector(".navv");
btn.addEventListener("click", () => {
    let isAgree = nav.classList.contains("active");
    if (isAgree) {
        nav.style.display = "none";
        nav.classList.remove("active");
        btn.innerHTML = `<i class="fa-solid fa-bars"></i>`;
    } else {
        nav.style.display = "block";
        nav.classList.add("active");
        btn.innerHTML = `<i class="fa-solid fa-bars fa-rotate-90"></i>`;
    }
})



