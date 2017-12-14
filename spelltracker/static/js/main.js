var prepared =  $(".prepared")
var spent = $(".spent")
var remaining = $(".remaining")
var characterid = $("#characterid").first().val()


// Update remaining spells per day
function UpdateRemaining(){
    for(i=0; i<prepared.length; i++){
        remaining[i].value = parseInt(prepared[i].value) - parseInt(spent[i].value)
    }
}

function SyncSpells(){
    $.ajax(
        {
            url: '/ajax/update',
            data: {
                'characterid': characterid,
            },
            dataType: 'json',
           success: function(data){
               console.log('success')
           }
        }
    )
}


UpdateRemaining()
SyncSpells()