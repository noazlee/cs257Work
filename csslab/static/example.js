var heading = document.getElementById("hello")
heading.onmouseover = function(){
  heading.style.fontStyle = "italic";
}

function changeColor() {
  const the_heading = document.getElementById("hello");

  const r = Math.floor(Math.random()*256)
  const g = Math.floor(Math.random()*256)
  const b = Math.floor(Math.random()*256)

  the_heading.style.color = 'rgb(${r},${g},${b})';
}
