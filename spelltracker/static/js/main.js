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

function GetArrayElements(spellArray){
    var array = []
    for(i=0; i<spellArray.length; i++){
        array[i] = spellArray[i].value
    }
    return array
}

function SyncSpells(){
    UpdateRemaining()
    $.ajax(
        {
            url: '/ajax/update',
            data: {
                'characterid': characterid,
                'prepared': GetArrayElements(prepared),
                'spent': GetArrayElements(spent),
            },
            dataType: 'json',
           success: function(data){
               console.log('Success')
           }
        }
    )
}

function Setup(){
    UpdateRemaining()
    prepared.change(SyncSpells)
    spent.change(SyncSpells)
}

Setup()