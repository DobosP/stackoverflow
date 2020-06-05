$(document).ready(function() {

    var username = window.sessionStorage.getItem('username');
    var EventID = window.sessionStorage .getItem('EventID');

    $('#userName').text(username);

    $.ajax({
        method: "GET",
        url: '/getallproposals',

        data: {
            'username':username,
        },

        success: function(data) {
            console.log(data)
            let dropdown = $('#pclistproposals_bind');

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

    $('#ProposalDetails').on('click', function(e) {
    e.preventDefault();
        var ProposalID =  $( "#pclistproposals_bind").find(":selected").val();
        window.sessionStorage.setItem('ProposalID', ProposalID);
        var url = "http://localhost:8080/chair/selectedprop";
        $(location).attr('href',url);

    });

   $('#could_eval').on('click', function(e) {
    e.preventDefault();
        var ProposalID =  $( "#pclistproposals_bind").find(":selected").val();
        analyze(username,ProposalID,"could_eval");

    });
    $('#pleased_eval').on('click', function(e) {
        e.preventDefault();
            var ProposalID =  $( "#pclistproposals_bind").find(":selected").val();
            analyze(username,ProposalID,"pleased_eval");
    
        });
    $('#refuse_eval').on('click', function(e) {
        e.preventDefault();
            var ProposalID =  $( "#pclistproposals_bind").find(":selected").val();
            analyze(username,ProposalID,"refuse_eval");
    
    });
            
   
});


function analyze(username,ProposalID,Analyze){
   
    $.ajax({
        method: "POST",
        url: '/adpcmember',
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({
            'username':username,
            'ProposalID': ProposalID,
            'Analyze': Analyze

        }),
        dataType: "json",
        success: function(data) {
            $('#msg').html('<span style="color: green;">Proposal analyzed!</span>');


        },
        error: function(err) {
            console.log(err);
        }
    });

}