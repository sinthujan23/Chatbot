![Nexus AI](https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png)

# Nexus AI ChatBot

## Installation & Setup

[Install Python] https://www.python.org/downloads/

[Install pip]

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```
python3 get-pip.py
```

Ensure pip is installed by running the following command

```
pip --version
```

If you have Python & pip installed then check their version in the terminal or command line tools

```
python3 --version
```

```
pip --version
```

## Installing Dependencies

In your terminal run the requirements.txt file using this pip

```
pip install -r requirements.txt
```

## Running ChatBot Application in Terminal

```
cd into your directory
```

```
python3 app.py
```

## What you will create

In this tutorial, I will guide you through the process of building Nexus AI - an intelligent chatbot that can carry out meaningful conversations with users using advanced natural language processing.

We will be using Microsoft DialoGPT-medium, a sophisticated pre-trained language model that generates human-like responses with contextual understanding. The model will be integrated with Flask, a lightweight Python web framework, to create a responsive web application with real-time chat capabilities.

For the frontend, we'll build a modern, dark-themed interface using HTML5, CSS3 with gradient designs, and vanilla JavaScript for smooth interactions. The interface features typing indicators, emoji-enhanced responses, and a fully responsive layout.

Throughout this tutorial, you'll learn how to set up the development environment, handle AI model integration, create RESTful APIs with Flask, and design an engaging user interface. The chatbot will automatically greet users and maintain conversation context throughout the session.

By the end, you'll have a production-ready chatbot named Nexus AI that can engage in intelligent dialogues, understand context, and provide emoji-enhanced responses to create a more human-like interaction experience.

# AI Model Link

The Chatbot is powered by the Microsoft/DialoGPT-medium model.

```
https://huggingface.co/microsoft/DialoGPT-medium
```

# User Message HTML

```
var userHtml = '<div class="message user"><div class="message-content"><p>' + user_input + '</p><div class="message-time">'+ time +
    '</div></div></div>';
```

# Bot Response HTML

```
var botHtml = '<div class="message bot"><div class="message-content"><p>' + bot_response + '</p><div class="message-time">' + time + '</div></div></div>';
```

# Typing Indicator HTML

```
var typingHtml = '<div class="message bot" id="typingIndicator"><div class="message-content"><div class="typing-indicator"><div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div></div></div></div>';
```

# Key Features

- 🤖 **AI-Powered Conversations** - Microsoft DialoGPT-medium model
- 🎨 **Modern Dark Theme** - Gradient backgrounds and smooth animations
- 💬 **Real-time Chat** - Instant messaging with typing indicators
- 😊 **Smart Emoji System** - Context-aware emoji responses
- 📱 **Fully Responsive** - Works on desktop and mobile devices
- 💾 **Session Memory** - Maintains conversation context
- ⚡ **Fast & Lightweight** - Optimized Flask backend

# File Structure

```
Nexus-AI-ChatBot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css         # Modern CSS styling
└── templates/
    └── chat.html         # Chat interface template
```

# API Endpoints

- `GET /` - Serves the main chat interface
- `GET /greet` - Returns automatic greeting message
- `POST /get` - Processes messages and returns AI responses

# Technologies Used

- **Backend**: Flask web framework
- **AI Model**: Microsoft DialoGPT-medium
- **Frontend**: HTML5, CSS3, JavaScript
- **Deep Learning**: PyTorch, Transformers
- **Styling**: Custom CSS with gradient animations

Start chatting with Nexus AI and experience the future of conversational AI! 🚀