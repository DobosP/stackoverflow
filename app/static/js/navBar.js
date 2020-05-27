$(document).ready(function() {
        var isLoggedIn = localStorage.getItem('loggedin');
        
        if(isLoggedIn != 1) {
            return false;
        }
        var userName = localStorage.getItem('userName');

        $('#userName').text(userName);

		$('#logOutButt').on('click', function(e) {
		e.preventDefault();
            localStorage.setItem('loggedin', 0);
            $('#userName').text(userName,'');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

	});
});

