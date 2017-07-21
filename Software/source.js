function loginPressed(){
    document.getElementById("sidebar").style.width = "85%";
    document.getElementById("loginButton").style.visibility = "hidden";
    document.getElementById("loginBar").style.marginRight = "-27.5%";
    setTimeout(showElement,500);
}

function loaded(){
    loginPressed();
}

function showElement(){
    document.getElementById("loginMenu").style.visibility = "visible";
}
