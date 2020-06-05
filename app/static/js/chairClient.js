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
            var EventID =  $( "#chairconferencelist").find(":selected").val();
            window.sessionStorage .setItem('EventID', EventID);
            var url = "http://localhost:8080/chair/selectedconf";
            $(location).attr('href',url);

        });




});

