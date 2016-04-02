var small_nav_height = 60; // height of small navigation header

(function($){ // create closure so we can safely use $ as alias for jQuery
    function menu_main_click() {
        $('#menu-main').toggleClass('sp-menu-open');
        $('#menu-language').removeClass('sp-menu-open');
    }
    function menu_language_click() {
        $('#menu-language').toggleClass('sp-menu-open');
        $('#menu-main').removeClass('sp-menu-open');        
    }
    function resize_me() {
        // if ($(window).width() < 1024) {
            // var h = $(window).height() - $('.feature-container .fake-padding').height();
            var h = $('#header').height();
            $('.feature-container .fake-padding').height(h);
            $('.feature-container .cycle-slideshow').height($(window).height() - h);
            // if ($(window).width() >= 1024) {
            //     $('#header .logo img').height(.40*h);
            //     $('#header .slogan').css('font-size', 30 + 'px');
            // }
    }

    $(document).ready(function(){

        // main menu
        $('#menu-main-button').on('click touchend', menu_main_click);
        $('#menu-main').hover(menu_main_click);

        // language menu
        $('#menu-language-button').on('click touchend', menu_language_click);
        $('#menu-language').hover(menu_language_click);

        // snap scrolling
        $(document).scrollsnap({
            snaps: '.snap',
            proximity_top: 200,
            proximity_bottom: 0,
            offset: -small_nav_height, 
            duration: 500,
            // easing: 'easeOutBack'
        });

        // page down buttons
        $('#cover .arrow-pagedown').click(function() {
            $(window).scrollTo({top: $('#sections').offset().top-small_nav_height, left: 0 }, 500);
        });
        $('#sections .arrow-pagedown').click(function() {
            $(window).scrollTo({top: $('#subscribe').offset().top-small_nav_height, left: 0 }, 500);
            // $(window).scrollTo('#subscribe', 500);
        });


        // resize main feature
        $(window).resize(resize_me);
        resize_me();

        // social sharing
        $('#twitter').sharrre({
          share: {
            twitter: false
          },
          enableHover: false,
          enableTracking: true,
          // buttons: { twitter: {via: '_JulienH'}},
          click: function(api, options){
            // api.simulateClick();
            api.openPopup('twitter');
          }
        });
        $('#facebook').sharrre({
          share: {
            facebook: false
          },
          enableHover: false,
          enableTracking: true,
          click: function(api, options){
            // api.simulateClick();
            api.openPopup('facebook');
          }
        });

        // pagination
        $.endlessPaginate();

    });
})(jQuery);

// analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','http://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-62171853-1', 'auto');
  ga('send', 'pageview');
