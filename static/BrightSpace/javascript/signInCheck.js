document.getElementById("sign_in").addEventListener("submit",
    (event) => {
        event.preventDefault()
        let element = new FormData(event.target)
        let username = element.get("username")
        let password = element.get("password")
        let repeatPassword = element.get("repeatPassword")
        if (password != repeatPassword) {
            alert("Please enter the same password")
        } else if (password.length < 6 || password.length > 16) {
            alert("Password should be at least 6 characters and at most 16 characters")
        } else {
            let checkAvailability = async () => {
                let result = await fetch("checkAvailability", {
                    method: "POST",
                    body: JSON.stringify({
                        "name": element.get("username"),
                        "password": element.get("password")
                    })
                })
                let json = await result.json()
                if (json["status"] === 200 && json["statusText"] === "OK") {
                    if (json["canBeUsed"] === true) {
                        alert("ok")
                    } else {
                        alert("This username has been used")
                    }

                } else {
                    throw new Error()
                }
            }
            checkAvailability().catch(() => {
                location.reload()
            })
        }

    })