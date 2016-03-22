// TODO allow for x scrollsnapping
(function( $ ) {

    $.fn.scrollsnap = function( options ) {

        var settings = $.extend( {
            'snaps' : '*',
            // 'proximity' : 12,
            'proximity_top' : 12,
            'proximity_bottom' : 12,
            'offset' : 0,
            'duration' : 200,
            'easing' : 'swing',
        }, options);

        return this.each(function() {
            settings.proximity = Math.max(settings.proximity_top, settings.proximity_bottom)

            var scrollingEl = this;

            if  (scrollingEl.scrollTop !== undefined) {
                // scrollingEl is DOM element (not document)
                $(scrollingEl).css('position', 'relative');

                $(scrollingEl).bind('scrollstop', function(e) {

                    var matchingEl = null, matchingDy = settings.proximity + 1;

                    $(scrollingEl).find(settings.snaps).each(function() {
                        var snappingEl = this;
                        var dy = snappingEl.offsetTop - scrollingEl.scrollTop;

                        if (dy > 0) {
                            proximy_local = settings.proximity_top;
                        } else {
                            dy = -dy;
                            proximy_local = settings.proximity_bottom;
                        }
                        if (dy <= proximy_local && dy < matchingDy) {
                            matchingEl = snappingEl;
                            matchingDy = dy;
                        }
                    });

                    if (matchingEl) {
                        $(scrollingEl).animate({scrollTop: (matchingEl.offsetTop + settings.offset)}, settings.duration, settings.easing);
                    }

                });

            } else if (scrollingEl.defaultView) {
                // scrollingEl is DOM document
                $(scrollingEl).bind('scrollstop', function(e) {

                    var matchingEl = null, matchingDy = settings.proximity + 1;

                    $(scrollingEl).find(settings.snaps).each(function() {
                        var snappingEl = this;

                        var dy = $(snappingEl).offset().top - scrollingEl.defaultView.scrollY;

                        if (dy > 0) {
                            proximy_local = settings.proximity_top;
                        } else {
                            dy = -dy;
                            proximy_local = settings.proximity_bottom;
                        }
                        if (dy <= proximy_local && dy < matchingDy) {
                            matchingEl = snappingEl;
                            matchingDy = dy;
                        }
                    });

                    if (matchingEl) {
                        $('html, body').animate({scrollTop: ($(matchingEl).offset().top + settings.offset)}, settings.duration, settings.easing);
                    }

                });
            }

        });

    };

})( jQuery );
