let elem = document.getElementById("container");
if (elem.children.length === 0){
    let message_elem = document.createElement("h3");
    message_elem.innerHTML = "You don't have any posts yet..."
    message_elem.style.textAlign = "center";
    document.body.append(message_elem);
}
