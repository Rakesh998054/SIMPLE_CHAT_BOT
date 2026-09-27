##  🤖 AI Assistant
<p align="center"> <strong>A Simple AI Chatbot Powered by OpenRouter</strong> </p> <p align="center"> A modern, responsive, and interactive AI chatbot built using Streamlit and NVIDIA Nemotron 3 Ultra. </p>
📌 About The Project

AI Assistant is a simple web-based chatbot application that allows users to interact with an AI model through a clean and modern chat interface.

The application uses Streamlit for the user interface and OpenRouter to communicate with the NVIDIA Nemotron 3 Ultra model.

The chatbot supports real-time response streaming, conversation history, chat clearing, and secure API-key management.

✨ Features

🤖 AI-powered conversational chatbot

💬 Interactive chat interface

⚡ Real-time streaming responses

🧠 Conversation history

🗑️ Clear Chat functionality

🌙 Modern dark-themed UI

👤 User and AI avatars

⚙️ Sidebar settings

🔐 Secure API key configuration

❌ API error handling

📱 Responsive interface

🖥️ Application Preview
<p align="center"> <img src="YOUR_SCREENSHOT_URL" alt="AI Assistant Screenshot" width="850"> </p>

Replace YOUR_SCREENSHOT_URL with the URL of your uploaded application screenshot.

🧠 AI Model
NVIDIA Nemotron 3 Ultra

The application uses the NVIDIA Nemotron 3 Ultra model through OpenRouter.

Model:

nvidia/nemotron-3-ultra-550b-a55b:free

OpenRouter provides the API interface used by the application to communicate with the AI model.

🛠️ Technologies
Technology	Purpose
🐍 Python	Application development
🎈 Streamlit	Web interface
🔌 OpenAI Python SDK	API communication
🌐 OpenRouter	AI API provider
🧠 NVIDIA Nemotron	AI model
🎨 HTML / CSS	UI customization
🎨 User Interface

The application provides a clean dark-themed interface.

Header

The main page displays:

🤖 AI Assistant

with the subtitle:

Powered by OpenRouter

Chat Area

Users can send messages through the chat input and receive AI-generated responses.

User and assistant messages are displayed separately with custom styling and avatars.

Sidebar

The sidebar contains:

⚙️ Settings

🧠 Model information

🗑️ Clear Chat button

👨‍💻 Developer information

ℹ️ Application information

⚡ Streaming Responses

The chatbot displays AI responses progressively as they are generated.

This creates a more natural conversational experience because users do not have to wait for the complete response before seeing the beginning of the answer.

🧠 Conversation History

The application maintains conversation history using Streamlit session state.

This allows the AI model to receive previous messages as context during the current session.

🗑️ Clear Chat

The Clear Chat button allows users to remove the current conversation and start a new conversation.

The application restores the default AI instructions when the chat is cleared.

🔐 API Key Security

The OpenRouter API key is stored using Streamlit Secrets.

The API key should never be directly written inside the Python source code or uploaded to GitHub.

The secrets file should remain local:

.streamlit/secrets.toml

Make sure this file is included in .gitignore.

⚠️ Important

Never publish your real OpenRouter API key in a public repository.

📁 Project Structure
AI_Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── .streamlit/
    └── secrets.toml


.streamlit/secrets.toml should remain private and should not be committed to GitHub.

🚀 Installation
1. Clone the Repository

Clone the project from GitHub and open the project directory.

2. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

3. Install Dependencies

Install the required Python packages listed in requirements.txt.

4. Configure OpenRouter

Create your Streamlit secrets configuration and add your OpenRouter API key.

5. Run the Application

Start the Streamlit application and open the displayed local URL in your browser.

📦 Requirements

The project requires Python and the following main libraries:

Streamlit

OpenAI Python SDK

The complete dependency list is available in requirements.txt.

🔄 Application Workflow
User
  ↓
Streamlit Chat Interface
  ↓
Conversation History
  ↓
OpenRouter API
  ↓
NVIDIA Nemotron 3 Ultra
  ↓
Streaming Response
  ↓
AI Assistant

👨‍💻 Developer
Rakesh

🎓 B.Tech (ISE) Student

🏫 NMAMIT

This project was developed as an educational project for learning AI application development, API integration, and Streamlit web development.

🔮 Future Improvements

The project can be extended with:

🌐 Web search

📄 PDF document support

📎 File uploads

🖼️ Image understanding

🎙️ Voice input

🔊 Text-to-speech

💾 Persistent chat history

👥 User authentication

🔄 Multiple AI model selection

⚙️ Advanced model controls

📊 Token usage statistics

📱 Improved mobile experience

⚠️ Disclaimer

AI-generated responses may sometimes contain inaccurate or incomplete information.

Users should independently verify important information before relying on AI-generated responses.

📜 License

This project is created for educational and personal learning purposes.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

<p align="center"> <strong>🤖 AI Assistant — Simple. Interactive. Intelligent.</strong> </p>
