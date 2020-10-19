$(document).ready(function(){
    $('.delete4ever').hide()

    $('.up').click(function() {
        $(this).hide()
        $('.delete4ever').slideToggle("slow")
    })

    $(window).scroll(function() {   
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            $('.update-side').hide()
        }        
        if($(window).scrollTop() + $(window).height() != $(document).height()) {
            $('.update-side').show()
        }  
     });

    $('.comment_delete-wrap').click(function(){
        var data = $('#comment_info').serialize()
        $.ajax({
            method : "POST",
            url : $(this).parent().parent().attr('action'),
            data : data,
            success: $(this).parent().slideToggle()
        })
    })


})