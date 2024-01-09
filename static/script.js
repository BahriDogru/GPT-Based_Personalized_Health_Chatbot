document.getElementById('user-input').addEventListener('keydown', function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {
    // Capture the input value
    var userInput = document.getElementById('user-input').value;

    // Send a POST request to Flask server with user input
    var response = await fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    var chatBox = document.getElementById('chat-box');
    var systemMessage = document.getElementById('system-message');
    systemMessage.style.display = "none"; // Kullanıcı yazdığı anda ekranı temizler

    if (userInput.trim() !== "") {
        chatBox.innerHTML += '<p><strong>Siz:</strong> ' + userInput + '</p>';

        // Get the response from ChatGPT
        var jsonResponse = await response.json();
        var chatGptResponse = jsonResponse.message;
        chatGptResponse = chatGptResponse.replace(/\n/g, '<br>');

        // Display the response in the chat box
        chatBox.innerHTML += '<p><strong>HealtBot Mia:</strong> ' + chatGptResponse +'<p>';

        document.getElementById('user-input').value = '';
    }
}