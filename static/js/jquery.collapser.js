function ready(f){ /in/.test(document.readyState)?setTimeout('ready('+f+')',9):f() }

ready(function(){
	var cls = "collapser";
	$('head').append('<style id="customstylesheet">.'+cls+' { position: relative; } .'+cls+'-intro { position: relative; z-index: 0; } .'+cls+'-split { position: relative; } .'+cls+'-button { position: absolute; z-index: 2; } .'+cls+'-main {display: none;} .'+cls+'-open .'+cls+'-intro { display: none; } .'+cls+'-open .'+cls+'-main { display: block; }</style>');

	// We need to find every ellipsis element, slowly build up a fake version
	// of it with the same properties checking the height as we go.
	$('.'+cls).each(function(i){

		// Get the content that we will try to truncate
		// Replace newlines and tabs with spaces to split by
		var orig = $(this).text();
		var content = $(this).html().replace(/[\n\r\t]/g," ").replace(/ {2,}/g," ").replace(/<ul> <li>/g,"<ul><li>");

		// Get the lines limit (default 3)
		var max = parseInt($(this).attr('lines')) || 3;
		var more = $(this).attr('more') || "&#8595;";
		var less = $(this).attr('less') || "&#8593;";
		// Get the outer tag but remove the ellipsis class and the number of lines
		var tag = $("<div />").append($(this).clone()).html().replace(/^(<[^\>]+>).*(<[^\>]+>)$/,"$1$2").replace(new RegExp("(\\s"+cls+"|"+cls+"\\s)"),"").replace(new RegExp(" class=\""+cls+"\""),"").replace(/ lines="[0-9]*"/,"");
		// Build a placeholder version of the element
		var el = $(tag);
		// Place the placeholder before the real one
		$(this).before(el);
		var oldstr = "";
		var str = "";
		var p = 0;
		// Create a nearly empty element to see what height it will be
		el.html(' ');
		var h = el.outerHeight();
		var oldh = h;
		var shorten = true;
		// Step through the string adding each word one-by-one
		for(var lines = 0, i = 0; lines <= max && p < content.length; i++){
			// Get the index of the next space (starting at position=p)
			a = content.indexOf(" ",p);
			if(a < 0){
				a = content.length;
				str = content;
				shorten = false;
			}else{
				// Build the string up the end of this word and add the ellipsis
				// so that we take it into account
				str = content.substr(0,a);
				str = str.replace(/^ +$/,"");
				str += (str[str.length-1] != ">" && str.length > 0) ? "&#8230;" : "";
			}
			str = $("<div/>").html(str).html();
			// We should check for any unclosed HTML tags and close them in order
			el.html(str);
			// Get the new height of the element
			h = el.outerHeight();
			// If the height has changed, increment the number of lines
			if(h != oldh) lines++;

		if(content.indexOf('The students will learn the principle') > 0) console.log(h,lines,p,a,str,max)

			// If we have too many lines, use the previous version of the string
			if(lines > max){
				str = oldstr;
				el.html(str)
			}
			// Store the old string and height
			oldstr = str;
			oldh = h;

			// Set the new starting position
			p = a+1;
		}
		if(lines < max) shorten = false;
		repl = $(str).text()
		if(orig.indexOf(repl)==0) shorten = false;


		// Remove the fake element
		el.remove()
		// Build replacement content
		if(shorten){
			$(this).html('<button class="'+cls+'-button">'+more+'</button><div class="'+cls+'-intro">'+str+'</div><div class="'+cls+'-main">'+content+'</div>');
			$(this).css({'min-height':($(this).outerHeight())+'px'});
			$(this).find('.'+cls+'-intro').on('click',function(){
				$(this).parent('.'+cls).find('button.'+cls+'-button').trigger('click');
			})
			$(this).find('button.'+cls+'-button').on('click',function(){
				var el = $(this).parent('.'+cls);
				//var expand = el.find('.'+cls+'-intro').is(':visible');
				el.toggleClass(cls+'-open');
/*				$(this).html(expand ? less : more)
				var intro = el.find('.'+cls+'-intro');
				var full = el.find('.'+cls+'-main');
				if(expand){
					intro.hide();//intro.css({'position':'absolute'}).fadeOut(200);
					full.show();//full.slideDown(400);
				}else{
					intro.show();//intro.css({'position':'absolute'}).fadeIn(200);
					full.hide();//full.slideUp(400);
				}*/
			});
		}
	});
});
