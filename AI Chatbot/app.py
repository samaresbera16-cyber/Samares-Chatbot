from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot responses
responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "how are you": "I'm doing great! Thanks for asking 😄",
    "your name": "I'm Samares AI Bot 🤖",
    "who made you": "I was created by Samares using Python and Flask 🚀",
    "bye": "Goodbye! Have a great day 😊",
    "good morning": "Good Morning ☀️",
    "good night": "Good Night 🌙 Sweet dreams!",
    "what is python": "Python is a powerful programming language 🐍",
    "what is ai": "AI stands for Artificial Intelligence 🤖",
    "tell me a joke": "Why do programmers hate bugs? Because they take the byte out of them 😂",
    "what can you do": "I can chat with you, answer questions, and help you learn Python 🚀",
    "favorite language": "Obviously Python 😎",
    "thank you": "You're welcome ❤️",
    "i love python": "Python loves you too 🐍❤️",
    "what is flask": "Flask is a lightweight Python web framework 🌐",
    "what is github": "GitHub is a platform to store and manage code repositories 💻",
    "who are you": "I'm your personal AI chatbot assistant 🤖",
    "can you help me": "Of course! Tell me what you need 😊",
    "what is html": "HTML is used to create webpages 🌍",
    "what is css": "CSS is used to style webpages 🎨",
    "what is javascript": "JavaScript makes websites interactive ⚡",
    "what is your purpose": "My purpose is to help and chat with users 🤝",
    "do you know coding": "Yes! I know Python, JavaScript, HTML, CSS and more 💻",
    "are you real": "I'm virtual, but our conversation is real 😄",
    "who is samares": "Samares is an awesome developer 😎",
    "motivate me": "Success starts with consistency 🚀",
    "i am sad": "Don't give up. Better days are coming ❤️",
    "tell me something": "Practice coding daily and you'll improve fast 🚀",
    "open source": "Open source means code is publicly available for everyone 💡",
    "what is dsa": "DSA means Data Structures and Algorithms 📚",
    "what is machine learning": "Machine Learning allows systems to learn from data 🤖",
    "do you sleep": "Nope 😄 I'm always awake for you!",
    "how old are you": "Age doesn't apply to AI bots 😎",
    "what is your hobby": "Helping users and solving problems 💻",
    "sing a song": "La la la 🎵 I'm better at coding than singing 😂"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    reply = responses.get(user_message, "Sorry, I don't understand that.")

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)