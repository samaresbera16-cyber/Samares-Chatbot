async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const message = inputField.value;

    if (message.trim() === "") return;

    const chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `<div class="user-message">${message}</div>`;

    // Send to backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Bot reply
    chatBox.innerHTML += `<div class="bot-message">${data.reply}</div>`;

    inputField.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}