(function($){ // create closure so we can safely use $ as alias for jQuery
    $(document).ready(function(){
        // resize top bar on scroll
        $(document).on('scroll', function() {
            if($(document).scrollTop()>100){
                $('#header').addClass('small');
            } else {
                $('#header').removeClass('small');
            }
        });
    });
})(jQuery);
