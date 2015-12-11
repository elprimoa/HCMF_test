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

	$('#myModal').on('show.bs.modal', function (event) {
		  var button = $(event.relatedTarget); // Button that triggered the modal
		  var id = button.attr('id'); // Extract info from data-* attributes
		  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
		  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
		  var modal = $(this);
		  modal.find('#asignar').click(function() {
		  	var reclutador = $("#reclutador").val();
		  	if(reclutador === '') {
		  		return;
		  	}
		  	$.ajax({
				method: "PUT",
				url: '/fase1/vacante/',
				data: { 'id': id, 'reclutador': reclutador },
				beforeSend: function(xhr) {
			        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
			    },
			})
			.done(function() {
				location.reload();
			});
		  });
		  //modal.find('.modal-body input').val(recipient)
	})
	
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
		location.reload();
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