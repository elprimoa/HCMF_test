$(document).ready(function() {
	$( "#from" ).datepicker({
      defaultDate: "+1w",
      changeMonth: true,
      changeYear: true,
      onClose: function( selectedDate ) {
        $( "#to" ).datepicker( "option", "minDate", selectedDate );
      }
    });
    $( "#to" ).datepicker({
      defaultDate: "+1w",
      changeMonth: true,
      changeYear: true,
      onClose: function( selectedDate ) {
        $( "#from" ).datepicker( "option", "maxDate", selectedDate );
      }
    });
	$( "#from" ).datepicker("option", "dateFormat", "yy-mm-dd");
	$( "#to" ).datepicker("option", "dateFormat", "yy-mm-dd");

	
});

function eliminar(id, url) {
		$.ajax({
		method: "DELETE",
		url: url,
		data: { 'id': id },
		beforeSend: function(xhr) {
	        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
	    },
	})
	.done(function() {
		window.location = url;
	});
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}