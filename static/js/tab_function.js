$(document).ready(function(){
    //  tabs hide
    $('.tab-toggle01').hide()
    $('.tab-toggle02').hide()
    $('.tab-toggle03').hide()
    $('.tab-toggle04').hide()
    $('.tab-toggle05').hide()
    $('.tab-toggle06').hide()
    //  tabs open & close function
    // #1
    $(".num1").click(function () {
        var effect = 'slide';
        var options = { direction: $('#options').val() };
        var duration = 300;    
        $('.tab-toggle01').toggle(effect, options , duration);
        $('.num2').hide()
        $('.num3').hide()
        $('.num4').hide()
        $('.num5').hide()
    });
    $('.tag-close01').click(function(){
        $('.tab-toggle01').hide()
        location.reload();
    })
    // #2
    $(".num2").click(function () {
        var effect = 'slide';
        var options = { direction: $('#options').val() };
        var duration = 300;    
        $('.tab-toggle02').toggle(effect, options , duration);
        $('.num1').hide()
        $('.num3').hide()
        $('.num4').hide()
        $('.num5').hide()
    });

    $('.tag-close02').click(function(){
        $('.tab-toggle02').hide()
        location.reload();

    })
    // $(document).mouseup(function (e) { 
    //     if ($(e.target).closest(".tag-close01").length === 0) { 
    //         Typer().$(".tab-toggle01").hide(); 
    //         } 
    //     }).done(function() {
    //         location.reload()        
    // }); 

    // #3
    $(".num3").click(function () {
        var effect = 'slide';
        var options = { direction: $('#options').val() };
        var duration = 300;    
        $('.tab-toggle03').toggle(effect, options , duration);
        $('.num1').hide()
        $('.num2').hide()
        $('.num4').hide()
        $('.num5').hide()
    });

    $('.tag-close03').click(function(){
        $('.tab-toggle03').hide()
        location.reload();

    })
    // $(document).mouseup(function (e) { 
    //     if ($(e.target).closest(".tab-toggle03").length === 0) { 
    //         $(".tab-toggle03").hide(); 
    //     } 
    // }); 


    $(".num4").click(function () {
        var effect = 'slide';
        var options = { direction: $('#options').val() };
        var duration = 300;    
        $('.tab-toggle04').toggle(effect, options , duration);
        $('.num1').hide()
        $('.num2').hide()
        $('.num3').hide()
        $('.num5').hide()
    });

    $('.tag-close04').click(function(){
        $('.tab-toggle04').hide()
        location.reload();

    })
    // $(document).mouseup(function (e) { 
    //     if ($(e.target).closest(".tab-toggle04").length === 0) { 
    //         $(".tab-toggle04").hide(); 
    //     } 
    // }); 


    $(".num5").click(function () {
        var effect = 'slide';
        var options = { direction: $('#options').val() };
        var duration = 300;    
        $('.tab-toggle05').toggle(effect, options , duration);
        $('.num1').hide()
        $('.num2').hide()
        $('.num3').hide()
        $('.num4').hide()
    });

    $('.tag-close05').click(function(){
        $('.tab-toggle05').hide()
        location.reload();

    })
    // $(document).mouseup(function (e) { 
    //     if ($(e.target).closest(".tab-toggle05").length === 0) { 
    //         $(".tab-toggle05").hide(); 
    //     } 
    // }); 
    
    $('.num6').click(function(){
        $('.tab-toggle06').show()
    })
    $(document).mouseup(function (e) { 
        if ($(e.target).closest(".tab-toggle06").length 
                    === 0) { 
            $(".tab-toggle06").hide(); 
        } 
    }); 
 
    $('.tab_buttons-wrap').hide()
    $('.memo_frame').click(function() {
        $(this).next().slideToggle("fast")
    })
    $('.tab_buttons-wrap').hide()
    $('.memo_frame_condition').click(function() {
        $(this).next().slideToggle("fast")
    })
// temporary delete
    $(".tab_delete").click(function() {
        var data = $(this).parent().serialize()
        $.ajax({
            type:"POST",
            url: $(this).parent().attr('action'),
            data: data,
            success: $(this).parent().parent().parent().parent().hide()
        })          
    })


// memo-move from tab
    $(".tab_move").click(function() {
        var data = $(this).parent().serialize()
        $.ajax({
            type:"POST",
            url: $(this).parent().attr('action'),
            data: data,
            success: $(this).parent().parent().parent().hide()
        })          
    })


// memo-move from list
    $(".list_tab_move").click(function() {
        var data = $(this).parent().serialize()
        $.ajax({
            type:"POST",
            url: $(this).parent().attr('action'),
            data: data,                
        })
        location.reload();
    })
    $(".media_tab_move").click(function() {
        var data = $(this).parent().serialize()
        $.ajax({
            type:"POST",
            url: $(this).parent().attr('action'),
            data: data,                
        })
        location.reload();
    })


// in deleted page
    $('.result_item_frame').click(function() {
        $(this).next().slideToggle("fast")
    })

// memo-delete / permanent delete
$(".tab_delete_perm").click(function() {
    var data = $(this).parent().serialize()
    $.ajax({
        type:"POST",
        url: $(this).parent().attr('action'),
        data: data,
        success: $(this).parent().parent().parent().hide()
    })          
    })
})