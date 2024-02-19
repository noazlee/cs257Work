var heading = document.getElementById("hello")
heading.onmouseover = function(){
  if(heading.style.fontStyle == "italic"){
    heading.style.fontStyle = "normal";
  }else{
    heading.style.fontStyle = "italic";
  }
}