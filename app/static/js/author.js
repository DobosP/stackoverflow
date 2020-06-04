$(document).ready(function() {

    var username = window.sessionStorage .getItem('username');
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
            let dropdown = $('#conferencesjoined');

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

    $('#ConferencesJoined').on('click', function(e) {
        e.preventDefault();
        var EventID =  Number.parseInt($( "#conferencesjoined").value)
        window.sessionStorage.setItem('EventID', EventID);
        var url = "http://localhost:8080/author/acceptedconf";
        $(location).attr('href',url);

    });

    $.ajax({
        method: "GET",
        url: '/getallconferences',

        data: {
            'username':username,
            'loginas': loginas
        },

        success: function(data) {
            console.log(data)
            let dropdown = $('#conferencestojoin');

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

    $('#ConferencesToJoin').on('click', function(e) {
        e.preventDefault();
        var EventID =  Number.parseInt($( "#conferencestojoin").value)
        window.sessionStorage.setItem('EventID', EventID);
        $.ajax({
            method: "POST",
            url: '/addparticipant',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'username': username,
                'eventid': EventID,
                'loginas': loginas
            }),
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
        var url = "http://localhost:8080/author";
        $(location).attr('href',url);
    });

    $('#logOutButt').on('click', function(e) {
        e.preventDefault();
            window.sessionStorage .setItem('loggedin', 0);
            window.sessionStorage .setItem('userName', '');
            window.sessionStorage .setItem('logedinas', '');
            var url = "http://localhost:8080";
            $(location).attr('href',url);

        });


});