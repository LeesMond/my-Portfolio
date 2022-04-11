$(document).ready(function(){
  $("hh").hide();
  $("footer").click(function(){
    $(this).next().slideToggle(1500);
  });
});
