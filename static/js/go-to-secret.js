$(document).ready(function(){
     $(window).scroll(function () {
            if ($(this).scrollTop() > 50) {
                $('#go-to-secret').fadeIn();
            } else {
                $('#go-to-secret').fadeOut();
            }
        });
        // scroll body to 0px on click
        $('#go-to-secret').click(function () {
            $('#go-to-secret').tooltip('hide');
            location.href="/secret"
            $('body,html').animate({
                scrollTop: 0
            }, 800);
            return false;
        });
        
        $('#go-to-secret').tooltip('show');

});
