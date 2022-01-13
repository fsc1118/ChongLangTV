document.getElementById("login").addEventListener
("submit", (event) => {
    let element = new FormData(event.target)
    let password = element.get("password")
    let userName = element.get("userName")
    event.preventDefault()
    let validate = async () => {
        let res = await fetch("checkLogin", {
            method: "POST",
            body: JSON.stringify({
                "password": password,
                "userName": userName
            })
        })
        alert(res)
    }
    validate()
})