(function($){ // create closure so we can safely use $ as alias for jQuery
	$(document).ready(function(){
		// resize top bar on scroll
		var y = 0;
		var h1 = parseFloat($('.logo-el').css('height'));
		var h2 = 43;
		var mt = parseInt($('.logo').css('margin-top'));
		var down,f,h;
		function adjustHeader(){
			down = $(document).scrollTop() > y;
			y = $(document).scrollTop();
			f = Math.max(0,Math.min((215-small_nav_height-y)/(215-small_nav_height),1));
			h = Math.max(215-$(document).scrollTop(),small_nav_height);
			if(down || y >= 215) $('#header').addClass('small');
			else $('#header').removeClass('small');
			
			if(y < 215){
				$('.logo-el').css({'height':(h2 + f*(h1-h2))+'px'});
				$('.logo').css({'margin-top':(8 + f*(mt-8))+'px'});
				$('#header').css({'height':h+'px'});
			}else{
				$('.logo-el').css({'height':''});
				$('.logo').css({'margin-top':''});
				$('#header').css({'height':''});
			}
			return;
		}
		$(document).on('scroll', adjustHeader);
		adjustHeader();
    });
})(jQuery);
