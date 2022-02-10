$(document).ready(function(){
  $("hide").hide();
  $("click").click(function(){
    $(this).next().slideToggle(1500);
  });
});
