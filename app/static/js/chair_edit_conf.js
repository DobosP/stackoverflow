$(document).ready(function(){

    var username = window.sessionStorage.getItem('username');
    var loginas = window.sessionStorage .getItem('loginas');

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

            dropdown.append('<option selected="true" disabled>aaaaaaa</option>');
            dropdown.prop('selectedIndex', 0);
            $.each(data, function (key, entry) {
            dropdown.append($('<option></option>').attr('value', entry.Username).text(entry.Username));



           });
        }
    })
});