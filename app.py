import streamlit as st
from openai import OpenAI

# PAGE CONFIG
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS
st.markdown(
    """
    <style>

    /* Main application */
    .stApp {
        background-color: #0e1117;
    }

    /* Main container */
    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }

    /* Header */
    .app-header {
        text-align: center;
        padding: 10px 0 25px 0;
    }

    .app-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .app-subtitle {
        color: #9ca3af;
        font-size: 16px;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        padding: 12px 18px;
        border-radius: 15px;
        margin-bottom: 12px;
    }

    /* User message */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        background-color: #1f2937;
        margin-left: 18%;
    }

    /* Assistant message */
    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {
        background-color: #171b24;
        margin-right: 18%;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        border-radius: 15px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #11151c;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# HEADER
st.markdown(
    """
    <div class="app-header">
        <div class="app-title">🤖 AI Assistant</div>
        <div class="app-subtitle">
            Powered by OpenRouter
        </div>
    </div>
    """,
    unsafe_allow_html=True
)




# SIDEBAR
with st.sidebar:

    st.header("⚙️ Settings")

   
    # MODEL INFORMATION
    st.write("### Model")

    st.code(
        "Nemotron 3 Ultra",
        language="text"
    )

   
    # CONTROLS
    st.write("### Controls")

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Give clear, accurate and concise answers."
                )
            }
        ]

        st.rerun()

    st.divider()




    # DEVELOPER
    st.write("### 👨‍💻 Developer")

    st.markdown(
        "**Rakesh**"
    )

    st.caption(
        "🎓 B.Tech(ISE) Student"
    )

    st.caption(
        "🏫 NMAMIT"
    )

    st.divider()


    # APPLICATION INFORMATION
    st.caption(
        "AI responses are generated using the "
        "configured OpenRouter model."
    )


# API CONFIGURATION
try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"]
   
except Exception:

    st.error(
        "OpenRouter API key is missing. "
        "Add OPENROUTER_API_KEY to "
        ".streamlit/secrets.toml"
    )

    st.stop()


BASE_URL = "https://openrouter.ai/api/v1"

MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


# OPENAI CLIENT
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


# INITIALIZE CHAT HISTORY
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Give clear, accurate and useful answers."
            )
        }
    ]


# DISPLAY PREVIOUS MESSAGES
for message in st.session_state.messages:

    # Don't show system prompt
    if message["role"] == "system":
        continue

    role = message["role"]

    if role == "user":

        with st.chat_message(
            "user",
            avatar="👤"
        ):
            st.markdown(message["content"])

    elif role == "assistant":

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):
            st.markdown(message["content"])


# CHAT INPUT
user_input = st.chat_input(
    "Message AI Assistant..."
)


# PROCESS USER MESSAGE
if user_input:

    # -----------------------------------------------------
    # Display user message
    # -----------------------------------------------------

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(user_input)

    # -----------------------------------------------------
    # Save user message
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # -----------------------------------------------------
    # Generate AI response
    # -----------------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        response_placeholder = st.empty()

        try:

      
            # API REQUEST
            response = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                temperature=0.7,
                stream=True
            )

            # STREAM RESPONSE
            full_response = ""

            for chunk in response:

                try:

                    content = chunk.choices[0].delta.content

                    if content:

                        full_response += content

                        response_placeholder.markdown(
                            full_response + "▌"
                        )

                except (AttributeError, IndexError):

                    continue

            # Remove cursor
            response_placeholder.markdown(
                full_response
            )

          
            # SAVE AI RESPONSE
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": full_response
                }
            )

        
        # ERROR HANDLING
        except Exception as e:

            error_message = str(e)

            st.error(
                f"❌ API Error\n\n{error_message}"
            )