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



     // $(window).scroll(function() { 
     //  var top = $(document).scrollTop();
     //  if (top > 700) $('.career_menu').addClass('top_block_fixed');
     //  else $('.career_menu').removeClass('top_block_fixed');
     // });
    

   

    $(document).ready(function(){

       

         $('.career_menu a').click(function() {
            var target = $(this).attr('href');
            $('html, body').animate({
                scrollTop: $(target).offset().top - 130
            }, 800);
            return false;
        });


        $('.wrapper_block_previews .load-more').click(function(e) {
          e.preventDefault();
            $(this).parents('.wrapper_block_previews').addClass('all_open');
        });

         $('.section-careers .content-card .list-item-container .link-container a').on( "click", function(e) {
          e.preventDefault();
          $('.section-careers .content-card .thumbnailed-list .list-item').removeClass('active');
          $(this).parents('.list-item').addClass('active');

          $('html, body').animate({
                scrollTop: $('.video-container').offset().top - 60
          }, 300);
      
          var attrhref = $(this).attr('href');
          $('.image-container iframe')[0].src= attrhref;
        });

     


      


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

   //  $(function() {
   //     var topPos = $('.career_menu').offset().top - 60;
   //     $(window).scroll(function() {
   //         var top = $(document).scrollTop();
   //         if (top > topPos) { $('.career_menu').addClass('top_block_fixed'); } else { $('.career_menu').removeClass('top_block_fixed')}
   //     });
   // });


})(jQuery);

// analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','http://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-62171853-1', 'auto');
  ga('send', 'pageview');
