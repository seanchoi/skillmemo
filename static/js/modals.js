$(document).ready(function() {
    $('.modal-background').hide()
    $('.modal-background-settings').hide()
    $('.dm-modal').hide()
    $('.contact').click(function(){
        // $('.dm-modal').show()
        $('.modal-background').show()
        $('.dm-modal').show()
    })
    $('.dm-cancel').click(function(){
        $('.modal-background').hide()
        location.reload()
    })
    $(document).mouseup(function (e) { 
        if ($(e.target).closest('.dm-modal').length === 0) { 
            $('.modal-background').hide();
        } 
    }); 

    $('.dm_item_frame').click(function() {
        $(this).next().slideToggle("fast")
    })

    $('.account-delete').click(function() {
        $('.modal-background-settings').show()
    })
    $('.delete-modal-btn-cancel').click(function(){
        $('.modal-background-settings').hide()
        location.reload()
    })
    $(document).mouseup(function (e) { 
        if ($(e.target).closest('.delete-modal').length === 0) { 
            $('.modal-background-setting').hide();
        } 
    }); 
 
})