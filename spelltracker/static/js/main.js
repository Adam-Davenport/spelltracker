var prepared =  $(".prepared")
var spent = $(".spent")
var remaining = $(".remaining")

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
                'test': 'test client data'
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