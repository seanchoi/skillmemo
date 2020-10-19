$(document).ready(function ($) {
    
      var slideCount = $('#slider .first_ul li').length;
      var slideWidth = $('#slider .first_ul li').width();
      var slideHeight = $('#slider .first_ul li').height();
      var sliderUlWidth = slideCount * slideWidth;
      
      $('#slider').css({ width: slideWidth, height: slideHeight });
      
      $('#slider .first_ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });
      
      $('#slider .first_ul li:last-child').prependTo('#slider .first_ul');
  
      function moveLeft() {
          $('#slider .first_ul').animate({
              left: + slideWidth
          }, 200, function () {
              $('#slider .first_ul li:last-child').prependTo('#slider .first_ul');
              $('#slider .first_ul').css('left', '');
          });
      };
  
      function moveRight() {
          $('#slider .first_ul').animate({
              left: - slideWidth
          }, 200, function () {
              $('#slider .first_ul li:first-child').appendTo('#slider .first_ul');
              $('#slider .first_ul').css('left', '');
          });
      };
  
      $('.control_prev').click(function () {
          moveLeft();
      });
  
      $('.control_next').click(function () {
          moveRight();
      });


    //   slider 02 
    var slideCount02 = $('#slider02 .second_ul li').length;
    var slideWidth02 = $('#slider02 .second_ul li').width();
    var slideHeight02 = $('#slider02 .second_ul li').height();
    var sliderUlWidth02 = slideCount02 * slideWidth02;
    
    $('#slider02').css({ width: slideWidth02, height: slideHeight02 });
    
    $('#slider02 .second_ul').css({ width: sliderUlWidth02, marginLeft: - slideWidth02 });
    
    $('#slider02 .second_ul li:last-child').prependTo('#slider02 .second_ul');

    function moveLeft02() {
        $('#slider02 ul').animate({
            left: + slideWidth02
        }, 200, function () {
            $('#slider02 .second_ul li:last-child').prependTo('#slider02 .second_ul');
            $('#slider02 .second_ul').css('left', '');
        });
    };

    function moveRight02() {
        $('#slider02 .second_ul').animate({
            left: - slideWidth02
        }, 200, function () {
            $('#slider02 .second_ul li:first-child').appendTo('#slider02 .second_ul');
            $('#slider02 .second_ul').css('left', '');
        });
    };

    $('.control_prev02').click(function () {
        moveLeft02();
    });

    $('.control_next02').click(function () {
        moveRight02();
    });
  
  });    
  