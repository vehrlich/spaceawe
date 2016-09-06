// Create a fake element with the ID+class of the main navigation 
// header to find what its height is defined as in the style sheet
var small_nav_height = parseInt($('<div id="header" class="small"></div>').css('height')) || 60;

// Create closure so we can safely use $ as alias for jQuery
(function($){

	function spaceAwareness(){
		this.pushstate = !!(window.history && history.pushState);
		var _obj = this;

		$('a').each(function(e){
			var href = $(this).attr('href');
			// Any links on the page that go to page anchors on this page,
			// except placeholder anchors, need to stop the default behaviour
			if(href.indexOf('#') >= 0 && href != "#"){
				// Attach a click event
				$(this).on('click',function(e){
					// Stop the default behaviour
					e.preventDefault();
					e.stopPropagation();
					// Update the history state
					history.pushState({},"SpaceAwareness",href);
					// Do the navigation step
					_obj.navigate(e);
				});
			}
		});
		// Any anchor changes (say by manual edit of the URL bar) need to have the navigation function called
		window[(this.pushstate) ? 'onpopstate' : 'onhashchange'] = function(e){ _obj.navigate(e); };

		// A function that scrolls down/up the page to the anchor point
		this.navigate = function(e){
			
			// Find the anchor point
			var anchor = location.href.split("#")[1];

			// Get the y location of this anchor
			var y = 0;
			if(anchor){
				if($('#'+anchor).length == 1){
					y = $('#'+anchor).offset().top;
					if(anchor != "main") y -= small_nav_height;
				}else{
					y = -1;
				}
			}

			if(y >= 0) $('html, body').animate({ scrollTop: y }, 800);
		}
		return this;
	}
	
	function menu_main_click() {
		$('#menu-main').toggleClass('sp-menu-open');
		$('#menu-language').removeClass('sp-menu-open');
	}
	function menu_language_click() {
		$('#menu-language').toggleClass('sp-menu-open');
		$('#menu-main').removeClass('sp-menu-open');        
	}
	function resize_me() {
		var h = $('#header').height();
		$('.feature-container .fake-padding').height(h);
		$('.feature-container .cycle-slideshow').height($(window).height() - h);
	}

	$(document).ready(function(){

		var space = new spaceAwareness();

		if($("div").is(".section-scoops ")) $('.section-scoops .pure-u-1 .list-item-container .title').matchHeight(false);
		
		if($("div").is(".section-activities")) $('.section-activities .pure-u-1 .list-item-container .title').matchHeight(false);

/*
		$('.career_menu a').click(function() {
			var target = $(this).attr('href');
			$('html, body').animate({
				scrollTop: $(target).offset().top - 130
			}, 800);
			return false;
		});
*/
		$('.close_search').click(function(e) {
			e.preventDefault();
			$('.search_head').removeClass('open');
		});

		$('.search_btn.closed').click(function(e) {
			e.preventDefault();
			$('.search_head').addClass('open');
		});

       

          // if($('.filter_search').val() != ''){
          // $('.filter_search').addClass('empty_field');
          //     } else {
          // $('.filter_search').removeClass('empty_field');
          //     }



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

      
        $('.to_top').click(function() {
          $('html, body').animate({
              scrollTop: 0
          }, 'slow');
          return false;

      });  

      $('.lang_btn').click(function(e) {
          e.preventDefault();
          $(this).next().toggle();
      });  

      $('.section-news .select_language .sp-links a').click(function(e) {
          e.preventDefault();
          var selectName = $(this).html();
          $(this).parent('.sp-links').prev().html(selectName);
      });  

      $(document).click(function(event) {
          if ($(event.target).closest('.select_language').length == 0) {
              $('.select_language .sp-links').fadeOut();
            }
      });


        // main menu
        $('#menu-main-button').on('click touchend', menu_main_click);
        $('#menu-main').hover(menu_main_click);

        // language menu
        $('#menu-language-button').on('click touchend', menu_language_click);
        //$('#menu-language').hover(menu_language_click);

        // snap scrolling
        /*$(document).scrollsnap({
            snaps: '.snap',
            proximity_top: 200,
            proximity_bottom: 0,
            offset: -small_nav_height, 
            duration: 500,
            // easing: 'easeOutBack'
        });*/

/*
        // page down buttons
        $('#cover .arrow-pagedown').click(function() {
            $(window).scrollTo({top: $('#sections').offset().top-small_nav_height, left: 0 }, 500);
        });
*/
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
