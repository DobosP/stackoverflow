$(document).ready(function(){

    var username = window.sessionStorage.getItem('username');
    var EventID = window.sessionStorage .getItem('EventID');
    console.log(EventID)
    $.ajax({
        method: "GET",
        url: '/geteventinfo',

        data: {
            'EventID':EventID
        },

        success: function(data) {
            console.log(data)
            data = data[0]
            $('#conferencename').val(data['conferencename'])
            $('#conferencetime').val(data['conferencetime'])
            $('#conferencecall').val(data['conferencecall'])
            $('#conferencedeadlines').val(data['conferencedeadlines'])
        
    
        },
        statusCode: {
            404: function(mesage) {
                console.log(mesage);
            }
        },
        error: function(err) {
            console.log(err);
        }
    });


    $.ajax({
        method: "GET",
        url: '/getusers',

        data: {
            'username': username
        },

        success: function(data) {
            console.log(data)
            let dropdown = $('#conferencepc');

            dropdown.empty();

            dropdown.append('<option selected="true" disabled>Users</option>');
            dropdown.prop('selectedIndex', 0);
            $.each(data, function (key, entry) {
            dropdown.append($('<option></option>').attr('value', entry.Username).text(entry.Username));

           });
        }
    })


    $('#updatepage').on('click', function(e) {
        e.preventDefault();
        var conferencename = $('#conferencename').val();
		var conferencetime = $('#conferencetime').val();
        var conferencecall = $('#conferencecall').val();
        var conferencedeadlines = $('#conferencedeadlines').val();
        var conferencepc = $('#conferencepc').val();



		if(conferencename != "" || conferencetime != "" ) {
			$.ajax({
				method: "POST",
				url: '/createconf',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({
                    'chair':username,
                    'EventID':EventID,
					'conferencename': conferencename,
					'conferencetime': conferencetime,
                    'conferencecall': conferencecall,
                    'conferencedeadlines': conferencedeadlines,
					'conferencepc': conferencepc,


				}),
				dataType: "json",
				success: function(data) {
					var url = "http://localhost:8080/chair";
					$(location).attr('href',url);

				},
				statusCode: {
					400: function() {
						$('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
					}
				},
				error: function(err) {
					console.log(err);
				}
			});

		} else {
			$('#msg').html('<span style="color: red;">Invalid username and password</span>');
		}
	});
});