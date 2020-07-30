
window.onload = function(){
    
 $.getScript('assests/js/jquery.min.js',function(){

 $.getScript('assests/js/index.js',function(){

 $.getScript('assests/js/bootstrap.min.js',function(){
        
            $(function(){           
                $("#chat").load("http://10.10.226.79/index.php"); 
                });
             }); 
          });
       });
     };