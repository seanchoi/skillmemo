$(document).ready(function(){
    $('fa-youtube').hide()
    $('.view_desc').mouseover(function(){
        $('.section-deco').css({
            "box-shadow": "5px 5px 7px #dcdcdc",
            "transition":"350ms ease-in-out"
        })
    });
    $('.view_desc').mouseout(function(){
        $('.section-deco').css({
            "box-shadow": "none",
            "transition":"350ms ease-in-out"
        })
    })

    $('.video_off01').click(function(){
        $('#ytplayer01').slideToggle()
    })    

    $('.video_off02').click(function(){
        $('#ytplayer02').slideToggle()
    })
    $('.video_off03').click(function(){
        $('#ytplayer03').slideToggle()
    })

    $('.bigsize-btn01').click(function(){
        $('.bigscreen-wrap').show().css("visibility","visible")
    })  

    $('.bigsize-btn02').click(function(){
        $('.bigscreen-wrap2').show().css("visibility","visible")
    })
    $('.bigsize-btn03').click(function(){
        $('.bigscreen-wrap3').show().css("visibility","visible")
    })
    $('.v01').click(function(){
        $('.bigscreen-wrap').hide().css("visibility","hidden")

    })
    $('.v02').click(function(){
        $('.bigscreen-wrap2').hide().css("visibility","hidden")

    })
    $('.v03').click(function(){
        $('.bigscreen-wrap3').hide().css("visibility","hidden")

    })

    dragElement(document.getElementById("bigscreen-wrap"));
  
    function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
        // if present, the header is where you move the DIV from:
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        // otherwise, move the DIV from anywhere inside the DIV:
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
    }
    };
})

