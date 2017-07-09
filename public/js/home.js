// TODO : Call this file only for home.html
// TODO : Find a way to get env

$(document).ready(function() {
    // Call API youtube video
    if($('#container-home')) {
        $.ajax("http://127.0.0.1:8000/api/homepage")
            .done(function(response) {
                if(response != undefined && response.video != undefined) {
                    var video = response.video;
                    var statusVideo = true;

                    if(video.indexOf("embed") >= 0) {
                        $('iframe').attr('src', 'video');
                    } else if(video.indexOf("watch") >= 0) {
                        video = video.replace('https://www.youtube.com/watch?v=', '//www.youtube.com/embed/') + '?rel=0';
                        $('iframe').attr('src', video);
                    } else {
                        statusVideo = false;
                    }

                    if(statusVideo) {
                        $('.preloader-wrapper').css('display', 'none');
                        $($('.video-container')[0]).css('display', 'inherit');
                    }
                }
            })
            .fail(function() {
                console.log('video non récupéré');
            })
            .always(function() {
                // Nothing todo
            });
    }

});
