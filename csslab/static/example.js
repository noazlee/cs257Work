var heading = document.getElementById("hello")
heading.onclick = function(){
  if(heading.style.fontStyle == "italic"){
    heading.style.fontStyle = "none";
  }else{
    heading.style.fontStyle = "italic";
  }
}