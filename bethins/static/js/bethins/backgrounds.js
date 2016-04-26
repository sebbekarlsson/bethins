function set_bg(element, src) {
    element.setAttribute('style', "background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)), url("+src+"); background-size: cover; background-repeat: no-repeat; background-position: center;");
}

window.onload = function () { 
    var elements = document.querySelectorAll('[bg]');
    
    for (var i = 0; i < elements.length; i++) {
        var el = elements[i];
        var src = el.getAttribute('bg');
        var slide = el.getAttribute('slide');

        if (slide != undefined) {
            if (slide != false && slide != 'False' && slide != 'false') {
                var srcs = src.split(',');
                set_bg(el, srcs[0]);
                el.setAttribute('image_id', 1);
                
                setInterval(function () {
                    var image_id = parseInt(el.getAttribute('image_id'));

                    set_bg(el, srcs[image_id]);
                    if (image_id  < srcs.length-1) {
                        image_id += 1;
                    } else {
                        image_id = 0;
                    }
                    el.setAttribute('image_id', image_id)
                }, 3000);
            }

            continue;
        }
        set_bg(el, src.replace("\n", ''));
    }
}
