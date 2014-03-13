       var show_menu = function()
       {
           $('.menu').css('width','285px');
           $('.menu').css('height','20px');
           $('.menu').html($('.parse_from_form').html());
           $('.menu').css('opacity','0.8');
           $('.menu').css('cursor','auto');
           $('.menu').unbind('click');
           $('div.input_meaning').click(choose_page_or_number);
    
       }
       var hide_menu = function()
       {
           $('.menu').html('>>');
           $('.menu').css('width','');
           $('.menu').css('height','hand');
           $('.menu').css('opacity','0.5');
           $('.menu').css('cursor','hand');
           $('.menu').click(show_menu);
       }
       var choose_page_or_number = function()
       {
           //var alter="Post number";
           if($(':input.parse_from').attr("name")=="parse_from")
           {
//<input type="text" class="parse_from float-left" 
//name="parse_from" 
//value="Parse from" 
//onfocus=";this.value='';" 
//onblur="if (this.value == '') this.value='Parse from';"/>                
                $(':input.parse_from').attr("name","page");
                $(':input.parse_from').attr("value","Page");
                $(':input.parse_from').attr("onblur","if (this.value == '') this.value='Page';");
                $('span.input_meaning').html("parse from");
            }
            else
            {
                $(':input.parse_from').attr("name","parse_from")
                $(':input.parse_from').attr("value","Parse from");
                $(':input.parse_from').attr("onblur","if (this.value == '') this.value='Parse from';");
                $('span.input_meaning').html("page");
            }
          
       }
       var hide = function()
       {
           //$(this).parent().parent().children().css('border','3px dotted yellow');
            var elem = $(this).parent().parent().children().eq(1);
            if (elem.is(":hidden")) {
              elem.slideDown();
              $('.hide_button',elem.parent()).html('-'); //margin:-7px 0px 0px -1px;
              $('.hide_button',elem.parent()).css('margin','-7px 0px 0px -1px');              
            } else {
              elem.slideUp();
              $('.hide_button',elem.parent()).html('+');
              $('.hide_button',elem.parent()).css('margin','-6px 0px 0px 0px');
            }
       }
       
       //$('[id^="post"]').css('border','3px dotted black');
       $('[id^="post"]').each(function(){
           //alert(22);
           //$(this).children().eq(0).children().eq(2).css('border','3px dotted red');
           $(this).children().eq(0).children().eq(2).click(hide);
           });
    $('.menu').click(show_menu);
    $('[id^="post"]').click(hide_menu);
    $('body').click(function(){document.location="program:/body-click"});
    $(document).keyup(function(e) {
        //if(e.which==76){document.location="program:/lock"}
        if (e.keyCode == 27) { document.location="program:/hide"}   // esc
    });
