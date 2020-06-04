$(document).ready(function() {

    var isLoggedIn = window.localstorage.getItem('loggedin');
    var username = window.localstorage.getItem('username');
    var loginas = window.localstorage.getItem('loginas');

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
            let dropdown = $('#pclistconferences');

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
            window.localstorage.setItem('loggedin', 0);
            window.localstorage.setItem('userName', '');
            window.localstorage.setItem('logedinas', '');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

        });


});