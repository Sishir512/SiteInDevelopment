

(function($){
  $(function(){

    $('.sidenav').sidenav();

    //init carasoules
    
    
      $('.slider').slider({
        fullWidth: true,
        indicators: false,
        height: 617
        
      });

      $('.sliderb').slider({
        fullWidth: true,
        indicators: false,
        height: 284
        
      });
      
      $('.sliderv').slider({
        fullWidth: true,
        indicators: false,
        height: 340
        
      });
      
      $('.venobox').venobox({

        closeColor : '#ffffff',
        spinColor : '#ffffff',
        arrowsColor :'#ffffff',
        
      });

        $('textarea#textarea2').characterCounter(); 

         

      
  
     
        $('.tabs').tabs();



        

  }); // end of document ready
})(jQuery); // end of jQuery name space




    
