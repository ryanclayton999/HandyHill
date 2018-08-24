<script src="http://code.jquery.com/jquery-2.2.0.js"></script>
<script src="http://code.jquery.com/ui/2.2.0/jquery-ui.js"></script>

$(document).ready(function () {

    $(".button-collapse").sideNav();

    $('.slider').slider();
});

// Initializes PhotoSwipe.
var pswpInit = function (startsAtIndex) {

    if (!startsAtIndex) {
        startsAtIndex = 0;
    }

    var pswpElement = document.querySelectorAll('.pswp')[0];

    // commented the array bellow since the images array will be loaded from the server
    // in variable called djangoAlbumImages.

    // build items array
    //var items = [
    //    {
    //        src: 'https://placekitten.com/600/400',
    //        w: 600,
    //        h: 400
    //    },
    //    {
    //        src: 'https://placekitten.com/1200/900',
    //        w: 1200,
    //        h: 900
    //    }
    //];

    // find is images are loaded from the server.
    if (window.djangoAlbumImages && window.djangoAlbumImages.length > 0) {
        // define options (if needed)
        var options = {
            // optionName: 'option value'
            // for example:
            index: startsAtIndex // start at first slide
        };

        // Initializes and opens PhotoSwipe
        var gallery = new PhotoSwipe(pswpElement, PhotoSwipeUI_Default, window.djangoAlbumImages, options);
        gallery.init();
    }
}
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}