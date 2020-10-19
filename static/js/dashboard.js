$(document).ready(function(){
    $('.account_menu-wrap').hide()
    $('.tab_buttons-wrap-media-dash').hide()
    $('.profile_link').click(function() {
        $('.account_menu-wrap').show()
    })
    $(document).mouseup(function (e) { 
    if ($(e.target).closest('.account_menu-wrap').length === 0) { 
        $('.account_menu-wrap').hide(); 
    } 
    }); 
    $('.search_bar').keyup(function(){
        var search_keyword = $('#search').serialize()
        $.ajax({
            method: "POST",
            url:$(this).next().attr('value'),
            data: search_keyword
        })
        .done(function(res){
            $('.search_preview').html(res)
        })
    })
    $('.list_view_from_media').hide()
    $('.list_btn_from_media').click(function() {
        $('.media_view_from_media').hide()
        $('.list_view_from_media').show()
    })
    $('.media_btn_from_media').click(function() {
        $('.media_view_from_media').show()
        $('.list_view_from_media').hide()
    })
    $('.media_view_from_list').hide()
    $('.media_btn_from_list').click(function() {
        $('.list_view_from_list').hide()
        $('.media_view_from_list').show()
    })
    $('.list_btn_from_list').click(function() {
        $('.list_view_from_list').show()
        $('.media_view_from_list').hide()
    })
    $('.memo-dash-option').click(function(){
        $(this).next().slideToggle("fast")
    })
    $('.go-back-dashboard').click(function() {
        history.back()
    })


})