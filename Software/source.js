function loginPressed(){
    document.getElementById("sidebar").style.width = "85%";
    document.getElementById("loginButton").style.visibility = "hidden";
    document.getElementById("loginBar").style.marginRight = "-27.5%";
}

function loaded(){
    loginPressed();
}
