$(document).ready(function() {

    var username = window.sessionStorage.getItem('username');
    var EventID = window.sessionStorage .getItem('EventID');

    $.ajax({
        method: "GET",
        url: '/getproposalinfo',

        data: {
            'username':username,
            'EventID':EventID
        },

        success: function(data) {
            console.log(data)
            $('#proposalname').text(data['proposalname'])
            $('#propsaltopic').text(data['propsaltopic'])
            $('#papertext').text(data['papertext'])
            $('#abstracttitle').text(data['abstracttitle'])
            $('#abstractname').text(data['abstractname'])
            $('#abstractpurpose').text(data['abstractpurpose'])
            $('#abstractmethods').text(data['abstractmethods'])
           
        },
        statusCode: {
            404: function(mesage) {
                console.log(mesage);
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



    $('#updateproposal').on('click', function(e) {
        e.preventDefault();
        var proposalname = $('#proposalname').val();
		var propsaltopic = $('#propsaltopic').val();
        var proposalauthors = $('#proposalauthors').val();
        var papertext = $('#papertext').val();
        var abstracttitle = $('#abstracttitle').val();
        var abstractname = $('#abstractname').val();
        var abstractpurpose = $('#abstractpurpose').val();
        var abstractmethods = $('#abstractmethods').val();

        $.ajax({
            method: "POST",
            url: '/upproposal',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'username':username,
                'EventID': EventID,
                'proposalname': proposalname,
                'propsaltopic': propsaltopic,
                'proposalauthors': proposalauthors,
                'papertext': papertext,
                'abstracttitle': abstracttitle,
                'abstractname': abstractname,
                'abstractpurpose': abstractpurpose,
                'abstractmethods': abstractmethods
            }),
            dataType: "json",
            success: function(data) {
                var url = "http://localhost:8080/author";
                $(location).attr('href',url);

            },
            statusCode: {
                400: function() {
                    $('#msg').html('<span style="color: red;">Bad request - invalid parameters</span>');
                }
            },
            error: function(err) {
                console.log(err);
            }
        });

		
	});


});

