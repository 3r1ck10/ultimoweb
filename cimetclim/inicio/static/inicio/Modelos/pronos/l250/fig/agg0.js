$(function () {
  $('.pr-price').hide();
  $('.d1').show();

  $('#seleccion').on("change",function () {
    $('.pr-price').hide();
    $('.d'+$(this).val()).show();
  }).val("1");
});
