document.getElementById("login").addEventListener
("submit", (event) => {
        let element = new FormData(event.target)
        let password = element.get("password")
        let username = element.get("username")
        event.preventDefault()
        let validate = async () => {
            let res = await fetch("checkLogin", {
                method: "POST",
                body: JSON.stringify({
                    "password": password,
                    "username": username
                })
            })
            let json = await res.json()

            if (json["isUsernameExist"]) {
                if (json["isPasswordMatch"]) {
                    alert("Good")
                } else {
                    alert("Unmatched Password")
                }
            } else {
                alert("No matching username found")
            }

        }
        validate().catch(() => {
            location.reload()
        })
    }
)