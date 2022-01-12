console.log("load")
document.getElementById("sign_in").addEventListener("submit",
    (event) => {
        let element = new FormData(event.target)
        let password = element.get("password")
        let repeatPassword = element.get("repeatPassword")
        if (password != repeatPassword) {
            alert("Please enter the same password")
            //location.reload()
            event.preventDefault()
        } else {
            /* check username availability*/
            let res = false
            let xhr = new XMLHttpRequest()
            xhr.open("Get", `checkAvailability/${element.get("userName")}`, false)

            xhr.onerror = () => {
                event.preventDefault()
                location.reload()
            }
            xhr.onload = () => {
                if (xhr.status == 200) {
                    console.log(xhr.responseText)
                    let json = JSON.parse(xhr.responseText)
                    console.log(json.result)
                    if (JSON.parse(json)["isAvailable"]) {
                        res = true
                    }
                    console.log(json["isAvailable"])
                    alert(json["isAvailable"])
                } else {
                    event.preventDefault()
                    location.reload()
                }
            }
            xhr.send()
            if (!res) {

                event.preventDefault()
            }
            alert("s")
        }
    })