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
                        "name": username,
                        "password": element.get("password")
                    })
                })
                result = await result.json()
                if (result["status"] === 200 && result["statusText"] === "OK") {
                    if (result["canBeUsed"] === true) {
                        let createUser = async () => {
                            result = await fetch("createUser", {
                                method: "POST",
                                body: JSON.stringify(
                                    {
                                        username: username,
                                        password: password
                                    }
                                )
                            })
                            let res = await result.json()
                  
                            if (res["status"] === 200 && res["statusText"] === "OK") {
                                alert("create successful")
                            } else {
                                throw new Error()
                            }
                        }
                        createUser().catch((error) => {
                            alert(error)
                            location.reload()
                        })
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