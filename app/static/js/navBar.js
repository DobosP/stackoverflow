$(document).ready(function() {
        var isLoggedIn = window.sessionStorage .getItem('loggedin');
        
        if(isLoggedIn != 1) {
            return false;
        }
        var userName = window.sessionStorage .getItem('userName');

        $('#userName').text(userName);

		$('#logOutButt').on('click', function(e) {
		e.preventDefault();
            window.sessionStorage .setItem('loggedin', 0);
            $('#userName').text(userName,'');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

	});
});

