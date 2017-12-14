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

function GetPrepared(){
    var array = []
    for(i=0; i<prepared.length; i++){
        array[i] = prepared[i].value
    }
}

function GetSpent(){
    var array = []
    for(i=0; i<spent.length; i++){
        array[i] = spent[i].value
    }
}

function SyncSpells(){
    $.ajax(
        {
            url: '/ajax/update',
            data: {
                'characterid': characterid,
                'prepared': GetPrepared(),
                'spent': GetSpent()
            },
            dataType: 'json',
           success: function(data){
               console.log(data)
           }
        }
    )
}


UpdateRemaining()
SyncSpells()