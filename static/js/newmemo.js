$(document).ready(function() {
    $('.style_options-wrap').hide()
    $('.style_options-wrap02').hide()
    $('.style_options-wrap03').hide()
    $('.code_editor-wrap').hide()

    // $('.add_3rd').hide()
    $('.content_2nd-wrap').hide()

    $('.add_2nd').click(function() {
        $('.content_2nd-wrap').slideToggle()
        $('.add_3rd').show()
    })
    $('.content_3rd-wrap').hide()
    $('.add_3rd').click(function() {
        $('.content_3rd-wrap').slideToggle()
    })

    // view code editor
    $('.code_editor_btn').click(function() {
        $('.code_editor-wrap').slideToggle()
    })


    // edit memo more content behavior
    $('.add_2nd_open').click(function() {
        $('.content_2nd-wrap_open').slideToggle()
    })
    
    $('.add_3rd_open').click(function() {
        $('.content_3rd-wrap_open').slideToggle()
    })

    // clear images
    $('.clear_images').click(function(){
        clearThumbnails(this, 'section1');
    });
    $('.clear_images02').click(function(){
        clearThumbnails(this, 'section2');
    });
    $('.clear_images03').click(function(){
        clearThumbnails(this, 'section3');
    });

    function clearThumbnails(self, sectionId) {
        $.ajax({
            method: "GET",
            url: $(self).prev().attr('value'),
        }).done(function(){
            $section = $('#' + sectionId);
            $section.find('.upload_img-wrap').empty()
            $section.find('.style_options-wrap').hide()
        })
    }

    
    
})