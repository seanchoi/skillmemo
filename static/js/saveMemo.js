$(document).ready(function(){
    // $('.memo-unsave-form-ajax').hide()
    $('.tab_buttons-wrap-savedmemo').hide()
    $('.save-btn').click(function() {
        var data = $(this).parent().parent().serialize()
        $.ajax({
            method:"POST",
            url:$(this).parent().parent().attr('action'),
            data:data,                 
            success: $(this).parent().parent().next().css('visibility', 'visible'),
          
        })
    })
    $('.unsave-btn').click(function() {
        var data = $(this).parent().parent().serialize()
        $.ajax({
            method:"POST",
            url:$(this).parent().parent().attr('action'),
            data:data,                 
            success: $(this).parent().parent().hide(),
        })
    })

    $('.save-btn-viewmemo').click(function() {
        var data = $(this).parent().parent().serialize()
        $.ajax({
            method:"POST",
            url:$(this).parent().parent().attr('action'),
            data:data,                 
            success: $(this).parent().parent().next().css('visibility', 'visible'),
          
        })
    })
    $('.unsave-btn-viewmemo').click(function() {
        var data = $(this).parent().parent().serialize()
        $.ajax({
            method:"POST",
            url:$(this).parent().parent().attr('action'),
            data:data,                 
            success: $(this).parent().parent().hide(),
        })
    })
})