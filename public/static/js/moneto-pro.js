document.addEventListener('DOMContentLoaded', function() {
    let username = "";
    let isWaitingForResponse = false; // Cooldown flag
    const usernameForm = document.getElementById("usernameForm");
    const chatContainer = document.getElementById("chat-container");
    const chatBox = document.getElementById("chat-box");
    const chatForm = document.getElementById("chatForm");
    const userInput = document.getElementById("userInput");
    const themeToggle = document.getElementById("themeToggle");
    const sendButton = chatForm.querySelector("button");

    // Theme toggle functionality
    initThemeToggle();

    // Username form submission
    usernameForm.addEventListener("submit", function(event) {
        event.preventDefault();
        username = document.getElementById("username").value.trim();
        if (username) {
            usernameForm.style.display = "none"; // Hide username form
            chatContainer.style.display = "flex"; // Show chat UI
            addMessage("bot", `### Hello, ${username}! How can I assist you today?`);
            setTimeout(() => userInput.focus(), 100); // Focus input field
        }
    });

    // Chat form submission
    chatForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        let message = userInput.value.trim();
        
        if (!message || isWaitingForResponse) {
            return; // Prevent empty messages or spamming
        }

        // Lock input while waiting for response
        isWaitingForResponse = true;
        userInput.disabled = true;
        sendButton.disabled = true;

        addMessage("user", `**${username}:** ${message}`);
        userInput.value = ""; // Clear input field

        // Show typing indicator
        showTypingIndicator();

        try {
            // Simulate network delay (1-2 sec)
            setTimeout(async () => {
                removeTypingIndicator();
                let botResponse = await sendToAI(username, message);
                addMessage("bot", botResponse);

                // Unlock input after response + 2-sec cooldown
                setTimeout(() => {
                    isWaitingForResponse = false;
                    userInput.disabled = false;
                    sendButton.disabled = false;
                    userInput.focus();
                }, 2000);
            }, 1000 + Math.random() * 1000);
        } catch (error) {
            removeTypingIndicator();
            addMessage("bot", "Error: Unable to contact AI service.");
            isWaitingForResponse = false;
            userInput.disabled = false;
            sendButton.disabled = false;
        }
    });

    // Initialize theme toggle
    function initThemeToggle() {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
            document.body.classList.add('dark-theme');
            themeToggle.innerHTML = '🌙';
        }

        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            const isDark = document.body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            themeToggle.innerHTML = isDark ? '🌙' : '☀️';
        });
    }

    // Create typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement("div");
        typingDiv.className = "typing-indicator";
        typingDiv.id = "typingIndicator";

        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('span');
            typingDiv.appendChild(dot);
        }

        chatBox.appendChild(typingDiv);
        scrollToBottom();
    }

    // Remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Scroll chat to bottom
    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Send message to AI backend
    async function sendToAI(username, message) {
        try {
            let response = await fetch("chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify({ username, message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            let data = await response.json();
            return data.response || "No response received.";
        } catch (error) {
            console.error("Error sending message to AI:", error);
            return "Error: Unable to contact AI service. Please try again later.";
        }
    }

    // Add chat message
    function addMessage(sender, text) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        const converter = new showdown.Converter();
        messageDiv.innerHTML = converter.makeHtml(text);
        chatBox.appendChild(messageDiv);
        scrollToBottom();
    }

    // Maintain scroll position on window resize
    window.addEventListener('resize', scrollToBottom);

    // Ensure input is always visible on mobile when keyboard appears
    userInput.addEventListener('focus', () => setTimeout(scrollToBottom, 300));
});
