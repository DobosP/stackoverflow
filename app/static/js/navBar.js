$(document).ready(function() {
        var isLoggedIn = window.localstorage.getItem('loggedin');
        
        if(isLoggedIn != 1) {
            return false;
        }
        var userName = window.localstorage.getItem('userName');

        $('#userName').text(userName);

		$('#logOutButt').on('click', function(e) {
		e.preventDefault();
            window.localstorage.setItem('loggedin', 0);
            $('#userName').text(userName,'');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

	});
});

