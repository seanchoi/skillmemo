$(document).ready(function () {

  // first section
    $(".upload_images_ajax").click(function () {
      $("#fileupload").click();
    });

    $("#fileupload").fileupload({
          dataType: 'json',
          done: function (e, data) {
            loadImage(data, 'section1', 4);
        }
    });

    // second section
    $(".upload_images_ajax_second").click(function () {
      $("#fileupload02").click();
    });

    $("#fileupload02").fileupload({
      dataType: 'json',
      done: function (e, data) {
        loadImage(data, 'section2', 4);
      }
    });

  // third section
    $(".upload_images_ajax_third").click(function () {
      $("#fileupload03").click();
    });

    $("#fileupload03").fileupload({
      dataType: 'json',
      done: function (e, data) {
        loadImage(data, 'section3', 2);
      }
    });
    
    function loadImage(data, sectionId, imgLimit) {
      var $section = $('#' + sectionId);
      var imgCount = $section.find('.upload_img_circle').length;
        if (imgCount < imgLimit){  
          if (data.result.is_valid) {
            $section.find(".upload_img-wrap").prepend(
              "<div class='upload_img_circle'><img class='upload_img' src='" + data.result.url + "'></div>"
            )
            $section.find('.style_options-wrap').show()
          }
          console.log('thumbname count', $section.find('.upload_img-wrap .upload_img_circle').length);
        }
    }
  });
  