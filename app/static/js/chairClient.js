$(document).ready(function() {
    $.ajax({
        method: "GET",
        url: '/getconferences',
        contentType: 'application/json;charset=UTF-8',
        
        dataType: "json",
        success: function(data) {
            console.log(data['message'])
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
    var isLoggedIn = localStorage.getItem('loggedin');
        
    // if(isLoggedIn != 1) {
    //     $("body").hide();
    // }
    var userName = localStorage.getItem('userName');

    $('#userName').text(userName);

    $.ajax({
        method: "GET",
        url: '/getconferences',
        contentType: 'application/json;charset=UTF-8',
        
        dataType: "json",
        success: function(data) {
            console.log(data)
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
        localStorage.setItem('loggedin', 0);
        localStorage.setItem('userName', '');
        var url = "http://localhost:8080";
        $(location).attr('href',url);

    });
    $('#logOutButt').on('click', function(e) {
        e.preventDefault();
            localStorage.setItem('loggedin', 0);
            localStorage.setItem('userName', '');
            var url = "http://localhost:8080";
            $(location).attr('href',url);
    
        });
    $('#createConf').on('click', function(e) {
        e.preventDefault();

            var url = "http://localhost:8080/chair/editconf";
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

