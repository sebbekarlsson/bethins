window.onload = function () { 
    var elements = document.querySelectorAll('[bg]');
    
    for (var i = 0; i < elements.length; i++) {
        var el = elements[i];
        var src = el.getAttribute('bg');
        el.setAttribute('style', "background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url('"+src+"'); background-size: cover; background-repeat: no-repeat; background-position: center;");
    }
}
