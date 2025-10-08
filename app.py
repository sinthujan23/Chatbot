from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import random

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)

# Store chat history for each session
chat_histories = {}

# Emoji categories for different contexts
emojis = {
    "greeting": ["👋", "😊", "🤖", "🌟", "💫"],
    "question": ["🤔", "💭", "🔍", "❓"],
    "positive": ["🎉", "👍", "✨", "😄", "👏"],
    "neutral": ["💬", "📝", "🔹", "👉"],
    "helpful": ["💡", "🚀", "🎯", "✅"],
    "funny": ["😄", "😂", "🤣", "🎭"],
    "tech": ["💻", "🔧", "⚡", "🔮"]
}

def add_emoji_to_response(text):
    """Add appropriate emojis to the response based on content"""
    text_lower = text.lower()
    
    # Greeting detection
    if any(word in text_lower for word in ['hello', 'hi', 'hey', 'greeting', 'welcome']):
        emoji = random.choice(emojis["greeting"])
    # Question detection
    elif any(word in text_lower for word in ['what', 'why', 'how', 'when', 'where', '?']):
        emoji = random.choice(emojis["question"])
    # Positive sentiment
    elif any(word in text_lower for word in ['great', 'awesome', 'good', 'excellent', 'perfect', 'amazing']):
        emoji = random.choice(emojis["positive"])
    # Helpful content
    elif any(word in text_lower for word in ['help', 'advice', 'suggestion', 'tip', 'guide']):
        emoji = random.choice(emojis["helpful"])
    # Tech-related
    elif any(word in text_lower for word in ['code', 'program', 'tech', 'computer', 'ai', 'bot']):
        emoji = random.choice(emojis["tech"])
    # Funny content
    elif any(word in text_lower for word in ['funny', 'joke', 'laugh', 'humor', 'haha']):
        emoji = random.choice(emojis["funny"])
    # Default neutral
    else:
        emoji = random.choice(emojis["neutral"])
    
    return f"{emoji} {text}"

def get_greeting():
    """Generate a random greeting with emoji"""
    greetings = [
        "Hello there! I'm Nexus AI, ready to chat with you! 👋",
        "Hi! I'm your friendly AI assistant. What would you like to talk about today? 😊",
        "Hey! Great to see you! I'm here to help with anything you need. 🤖",
        "Welcome! I'm Nexus AI, powered by Microsoft DialoGPT. How can I assist you? 💫",
        "Greetings! I'm excited to chat with you. What's on your mind? 🌟"
    ]
    return random.choice(greetings)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_Chat_response(msg)
    return response

@app.route("/greet", methods=["GET"])
def greet():
    """Endpoint to get initial greeting"""
    return get_greeting()

def get_Chat_response(text):
    """Generate chat response with emojis"""
    # Get session ID (simplified version)
    session_id = request.remote_addr
    
    # Initialize chat history for new session
    if session_id not in chat_histories:
        chat_histories[session_id] = None
    
    # Encode the new user input
    new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
    
    # Append to chat history or start new
    if chat_histories[session_id] is not None:
        bot_input_ids = torch.cat([chat_histories[session_id], new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids
    
    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    
    # Update chat history
    chat_histories[session_id] = chat_history_ids
    
    # Decode response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    # Add emoji to response
    response_with_emoji = add_emoji_to_response(response)
    
    return response_with_emoji

if __name__ == '__main__':
    app.run(debug=True)