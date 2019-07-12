setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);

 $(document).ready(function() {
    $("#MyModal").modal();
  });

  
  $('#checkbox-value').text($('#checkbox1').val());

$("#checkbox1").on('change', function() {
  if ($(this).is(':checked')) {
    $(this).attr('value', "True");
  } else {
    $(this).attr('value', "False");
  }
  
  $('#checkbox-value').text($('#checkbox1').val());
});