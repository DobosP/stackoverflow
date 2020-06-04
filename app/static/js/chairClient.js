$(document).ready(function() {

    var username = window.sessionStorage.getItem('username');
    var loginas = window.sessionStorage .getItem('loginas');

    $('#userName').text(username);

    $.ajax({
        method: "GET",
        url: '/getconferences',

        data: {
            'username':username,
            'loginas': loginas
        },

        success: function(data) {
            console.log(data)
            let dropdown = $('#chairconferencelist');

            dropdown.empty();

            dropdown.append('<option selected="true" disabled>Choose Conference</option>');
            dropdown.prop('selectedIndex', 0);
            $.each(data, function (key, entry) {
            dropdown.append($('<option></option>').attr('value', entry.EventID).text(entry.Name));
           });
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

    $('#logOutButt').on('click', function(e) {
        e.preventDefault();
            window.sessionStorage .setItem('loggedin', 0);
            window.sessionStorage .setItem('userName', '');
            window.sessionStorage .setItem('logedinas', '');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

        });
    $('#createConf').on('click', function(e) {
        e.preventDefault();

            var url = "http://localhost:8080/chair/editconf";
            $(location).attr('href',url);

    });

    $('#conferenceDetails').on('click', function(e) {
        e.preventDefault();
            var EventID =  Number.parseInt($( "#chairconferencelist").value)
            window.sessionStorage .setItem('EventID', EventID);
            var url = "http://localhost:8080/chair/selectedconf";
            $(location).attr('href',url);

        });


    $('#updatepage').on('click', function(e) {
        e.preventDefault();
        var conferencename = $('#conferencename').val();
		var conferencetime = $('#conferencetime').val();
        var conferencecall = $('#conferencecall').val();
        var conferencedeadlines = $('#conferencedeadlines').val();
        var conferencepc = $('#conferencepc').val();
        var conferencesections = $('#conferencesections').val();
        var conferenceprogram = $('#conferenceprogram').val();


		if(conferencename != "" || conferencetime != "" ) {
			$.ajax({
				method: "POST",
				url: '/createconf',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({
                    'chair':userName,
					'conferencename': conferencename,
					'conferencetime': conferencetime,
                    'conferencecall': conferencecall,
                    'conferencedeadlines': conferencedeadlines,
					'conferencepc': conferencepc,
                    'conferencesections': conferencesections,
                    'conferenceprogram': conferenceprogram

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

