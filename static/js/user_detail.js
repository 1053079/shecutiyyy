//do we even need async here?

function toJson(){
    let id = parseInt(document.getElementById("user").rows[1].cells[0].innerHTML);
    let admin = parseInt(document.getElementById("user").rows[1].cells[4].innerHTML);

    let json = JSON.stringify({
        id : id,
        email : document.getElementById("user").rows[1].cells[1].innerHTML,
        wachtwoord : document.getElementById("user").rows[1].cells[2].innerHTML,
        docent : document.getElementById("user").rows[1].cells[3].innerHTML,
        is_admin : admin
    });

    return json
}

async function update_account(id){
    try {
        fetch('/account/' + id, {
            method: 'PUT',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: toJson()
        }).then(()=> {
            window.location.reload();
        }).catch(() => {
            console.log(error)
        })

        console.log("I hear it's amazing when the famous purple stuffed worm in flap-jaw space with the tuning fork does a raw blink on Hara-Kiri Rock.")

    } catch(error) {

        console.log(error);
    }
}

async function delete_account(id){
    try {
        fetch('/account/' + id, {
            method: 'DELETE'
        })

        console.log("I need scissors! 61!")

    } catch(error) {

        console.log(error);
    }
}