// Define the minimum and maximum height of the header bar on this page
// These are dummy values; we'll get them from the CSS later
var nav_height = { 'small' : 60, 'big': 215 };

// Create closure so we can safely use $ as alias for jQuery
(function($){

	function spaceAwareness(){
		this.pushstate = !!(window.history && history.pushState);
		var _obj = this;

		$('a').each(function(e){
			var href = $(this).attr('href');
			// Any links on the page that go to page anchors on this page,
			// except placeholder anchors, need to stop the default behaviour
			if(href == window.location.pathname || href.indexOf("#")==0){
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
					if(anchor != "main") y -= nav_height.small;
				}else{
					y = -1;
				}
			}
			// If we want the top, that is at y = 0
			if(anchor == "top") y = 0;

			if(y >= 0) $('html, body').animate({ scrollTop: y }, 800);
		}
		return this;
	}

	function menu_main_click() {
		$('#menu-main').toggleClass('side-menu-open');
		$('#menu-language').removeClass('side-menu-open');
	}
	function menu_language_click() {
		$('#menu-language').toggleClass('side-menu-open');
		$('#menu-main').removeClass('side-menu-open');
	}
	//function menu_search_click() {
	//	$('#menu-search').toggleClass('side-menu-open');
	//	$('#menu-main').removeClass('side-menu-open');
	//}
	function resize_me() {
		var h = $('#header').height();
		$('.feature-container .fake-padding').height(h);
		$('.feature-container .cycle-slideshow').height($(window).height() - h);
	}

	function getStyleSheetPropertyValue(selectorText, propertyName) {
		// search backwards because the last match is more likely the right one
		for(var s= document.styleSheets.length - 1; s >= 0; s--) {
			// Use a try/catch to stop Firefox throwing a security error for stylesheets originating from a different domain.
			// See http://stackoverflow.com/questions/21642277/security-error-the-operation-is-insecure-in-firefox-document-stylesheets?noredirect=1&lq=1
			try {
				var cssRules = document.styleSheets[s].rules || document.styleSheets[s].cssRules
				for (var c=0; c < cssRules.length; c++) {
					if (cssRules[c].selectorText === selectorText) return cssRules[c].style[propertyName];
				}
			}catch(e){

			}
		}
		return null;
	}

	$(document).ready(function(){
		// Get current height of header bar
		var h = parseInt($('#header').css("height"));
		if(typeof h === "number") nav_height.big = h;
		// Get height it would have if the header bar was in compact mode
		var h = getStyleSheetPropertyValue('.header-small', "height");
		if(typeof h === "number") nav_height.small = h;

		var space = new spaceAwareness();

		// resize top bar on scroll
		var y = 0;
		var h1 = parseFloat($('.logo-el').css('height'));
		var h2 = 43;
		var mt = parseInt($('.logo').css('margin-top'));
		var down,f,h;
		function adjustHeader(){
			down = $(document).scrollTop() > y;

			y = $(document).scrollTop();
			// Fix for Safari that allows negative values of y to do 
			// a 'bounce' effect which will mess us up
			if(y <= 0){
				down = false;
				y = 0;
			}
			f = Math.max(0,Math.min((nav_height.big - nav_height.small - y)/(nav_height.big - nav_height.small),1));
			h = nav_height.big - $(document).scrollTop();
			if(h < nav_height.small) h = nav_height.small;

			if(down || y >= nav_height.big || nav_height.big==nav_height.small) $('body').addClass('menu-small');
			else $('body').removeClass('menu-small');

			if(y < nav_height.big){
				$('.logo-el').css({'height':(h2 + f*(h1-h2))+'px'});
				$('.logo').css({'margin-top':(8 + f*(mt-8))+'px'});
				$('#header').css({'height':h+'px','background-position': (100+(y/nav_height.big)*10)+'% center, left center'});
			}else{
				$('.logo-el').css({'height':''});
				$('.logo').css({'margin-top':(8 + f*(mt-8))+'px'});
				$('#header').css({'height':'','background-position': (100+(y/nav_height.big)*10)+'% center, left center'});
			}
			return;
		}
		$(document).on('scroll', adjustHeader);
		adjustHeader();

		$('.cycle-slideshow').slick({
			autoplay: true,
			// mobileFirst: true,
			prevArrow: '<div><img class="slick-prev" src="/static/img/arrow-image-prev.svg"></div>',
			nextArrow: '<div><img class="slick-next" src="/static/img/arrow-image-next.svg"></div>',
			dots: true,
			swipe: true,
			autoplaySpeed: 5000,
			pauseOnDotsHover: true,
		});

		if($("div").is(".section-scoops ")) $('.section-scoops .pure-u-1 .list-item-container .title').matchHeight(false);

		if($("div").is(".section-activities")) $('.section-activities .pure-u-1 .list-item-container .title').matchHeight(false);

		$('.close_search').click(function(e) {
			e.preventDefault();
			$('.search_head').removeClass('open');
		});

		$('.search_btn.closed').click(function(e) {
			e.preventDefault();
			$('.search_head').addClass('open');
		});


		$('.wrapper_block_previews .load-more').click(function(e) {
			e.preventDefault();
				$(this).parents('.wrapper_block_previews').addClass('all_open');
		});

		// Only target links in the video thumbnail list
		$('.section-careers .content-card .video_thumbnailed .list-item-container .link-container a').on( "click", function(e) {
			e.preventDefault();
			$('.section-careers .content-card .thumbnailed-list.video_thumbnailed .list-item').removeClass('active');
			$(this).parents('.list-item').addClass('active');

			$('html, body').animate({
						scrollTop: $('.video-container').offset().top - 60
			}, 300);

			var attrhref = $(this).attr('href');
			$('.image-container iframe')[0].src= attrhref;
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

		// language menu
		$('#menu-language-button').on('click touchend', menu_language_click);

		// language menu
		//$('#menu-search-button').on('click touchend', menu_search_click);

		$('#sections .arrow-pagedown').click(function() {
			$(window).scrollTo({top: $('#subscribe').offset().top - nav_height.small, left: 0 }, 500);
		});


        // search filters
        $(function() {
            $('ul.filter-select li').click(function(){
                $("input:checkbox[id='input-"+this.id+"']").attr('checked', true);
                $("#div-"+this.id).attr('hidden', false);
                $("#div-remove-all").attr('hidden', false);
                $(".selected-filters").attr('hidden', false);
            });
        });

        $(function() {
            $('.close-button').click(function(){
                // remove close-
                id = this.id.substr(6);
                $("input:checkbox[id='input-"+id+"']").attr('checked', false);
                $("#div-"+id).attr('hidden', true);
                // if there is not anything checked - hide remove all
                if ($(".selected-filters").find(".selected-filter").find("input:checked").length == 0) {
                    $("#div-remove-all").attr('hidden', true);
                    $(".selected-filters").attr('hidden', true);
                }
            });
        });

        // uncheck and hide all filter checkboxes when click on 'Remove all'
        $(function() {
            $('#div-remove-all').click(function(){
                $('input:checkbox[id*=input-]').attr('checked', false);
                $('input:checkbox[id*=input-]').parent().parent().attr('hidden',true);
                $("#div-remove-all").attr('hidden', true);
                $(".selected-filters").attr('hidden', true);
            });
        });

        $(function() {
            $('span.select-all').click(function() {
                // remove all-
                id = this.id.substr(4);
                // check all checkboxes depends on ID, show them and show 'Remove all' button
                $('input:checkbox[id*=input-'+id+'-]').attr('checked', true);
                $('input:checkbox[id*=input-'+id+'-]').parent().parent().attr('hidden',false);
                $("#div-remove-all").attr('hidden', false);
                $("#close-remove-all").attr('hidden', false);
                $(".selected-filters").attr('hidden', false);
            });
        });


      // show 'remove all filters' on page load if there is any active filter
        if ($(".selected-filters").find(".selected-filter").find("input:checked").length > 0) {
            $("#div-remove-all").attr('hidden', false);
            $(".selected-filters").attr('hidden', false);
        }

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
