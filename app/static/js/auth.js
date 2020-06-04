$(document).ready(function() {

	$('#loginSubmit').on('click', function(e) {
		e.preventDefault();
		
		var username = $('#usernamelogin').val();
		var pwd = $('#passwordlogin').val();
		var loginas =  $('#logInAs').val();
		
		var regex_email = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
		
		if(username != "" || pwd != "" ) {			
			$.ajax({
				method: "POST",
				url: '/login',
				contentType: 'application/json;charset=UTF-8',
				data: JSON.stringify({
					'username': username,
					'password': pwd,
					'loginas': loginas
				}),
				dataType: "json",
				success: function(data) {
					localStorage.setItem('loggedin', 1);
					localStorage.setItem('username', username);
					localStorage.setItem('loginas', loginas);
					var url = "http://localhost:8080/" + loginas;
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
	
	$('#signupSubmit').on('click', function(e) {
		e.preventDefault();
		
		var username = $('#usernamesignup').val();
		var email = $('#email').val();
		var pwd = $('#passwordsignup').val();
		var affiliation = $('#affiliation').val();
		
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
		
		if(email != "" && pwd != "" && username != "") {
			if(!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/signup',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({
						'username': username,
						'email': email,
						'password': pwd,
						'affiliation': affiliation}),
					dataType: "json",
					success: function(data) {
						$('#signupform').hide();
						$('#msg').html('<span style="color: green;">You are registered successfully</span>');
					},statusCode: {
						400: function() {
							$('#msg').html('<span style="color: red;">Bad request parameters</span>');
						},
						409 : function() {
							$('#msg').html('<span style="color: red;">You are already registered user</span>');
						}
					},
					error: function(err) {
						console.log(err);
					}
				});
			}
		} else {
			$('#msg').html('<span style="color: red;">All fields are required</span>');
		}
	});

});

