🤖 AI Assistant

A modern AI-powered chatbot built using Streamlit and OpenRouter. The application provides a simple, clean, and interactive chat interface for communicating with an AI model.

📌 Project Overview

AI Assistant is a web-based chatbot application designed to provide AI-generated responses through a user-friendly interface.

The application uses the OpenRouter API to connect with the NVIDIA Nemotron 3 Ultra model and supports real-time streaming responses.

✨ Features

🤖 AI-powered conversational chatbot

💬 Interactive chat interface

⚡ Real-time streaming responses

🧠 Conversation history during the session

🗑️ Clear Chat option

🌙 Modern dark-themed interface

🎨 Custom CSS styling

👤 User and AI avatars

⚙️ Sidebar settings panel

🔐 Secure API key configuration using Streamlit Secrets

❌ API error handling

📱 Responsive web interface

🧠 AI Model

The application uses:

NVIDIA Nemotron 3 Ultra 550B

The model is accessed through OpenRouter, which provides an API-compatible interface for interacting with the AI model.

🛠️ Technologies Used

Python — Application development

Streamlit — Web interface

OpenAI Python SDK — API client

OpenRouter — AI model API

NVIDIA Nemotron 3 Ultra — AI model

HTML/CSS — UI customization

🎨 User Interface

The application features a dark, modern interface with:

Centered AI Assistant title

OpenRouter-powered subtitle

Separate user and assistant chat bubbles

User 👤 and AI 🤖 avatars

Sidebar settings

Model information

Clear Chat button

Developer information

Chat input at the bottom

⚙️ Main Components
Chat Interface

Users can enter questions or messages through the chat input. The AI response is displayed immediately as it is generated.

Conversation History

The application maintains the conversation during the current Streamlit session, allowing the AI to use previous messages as context.

Streaming Response

AI responses are streamed gradually instead of appearing all at once, providing a smoother and more interactive experience.

Clear Chat

The Clear Chat button removes the existing conversation and starts a fresh session with the default AI instructions.

API Configuration

The OpenRouter API key is stored using Streamlit Secrets rather than being directly included in the application.

🔐 Security

The OpenRouter API key should be stored securely in Streamlit Secrets.

Do not upload your API key to GitHub or include it directly in your source code.

Make sure your secrets file is added to .gitignore.

🚀 Installation
Prerequisites

Before running the project, make sure you have:

Python 3.9 or later

An OpenRouter account

An OpenRouter API key

Setup

Clone or download the project.

Create a Python virtual environment.

Install the required dependencies.

Configure your OpenRouter API key using Streamlit Secrets.

Start the Streamlit application.

▶️ Running the Application

Launch the application using Streamlit.

Once started, open the local Streamlit URL displayed in your terminal.

The AI Assistant interface will then be available in your browser.

📁 Project Structure

The project can be organized as follows:

app.py — Main Streamlit application

requirements.txt — Python dependencies

.streamlit/secrets.toml — Private API configuration

README.md — Project documentation

👨‍💻 Developer

Rakesh

🎓 B.Tech (ISE) Student
🏫 NMAMIT

🔮 Future Improvements

Future versions of the project could include:

🌐 Web search

📄 PDF and document support

📎 File uploads

🖼️ Image input

🎙️ Voice input

🔊 Voice responses

💾 Persistent conversation storage

👥 User authentication

🔄 Multiple AI model selection

⚙️ Advanced model settings

📊 Token and usage statistics

📱 Improved mobile interface

⚠️ Disclaimer

AI-generated responses may occasionally contain inaccurate or incomplete information. Users should verify important information independently.

📜 License

This project is created for educational and personal learning purposes.

⭐ AI Assistant

A simple, modern, and interactive AI chatbot powered by Streamlit and OpenRouter.