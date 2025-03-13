import google.generativeai as genai
import gradio as gr
import os

# Set your Google Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBz3vwTB9kfTHbl_ILC3JLLt0ozKhalpBc"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the AI model with personality settings
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Track chat history to maintain context
chat_session = model.start_chat(history=[])

# Define chat function with personality
def chat_with_girlfriend(user_input, chat_history=[]):
    chat_history.append(("You", user_input))
    
    # Custom roleplay instructions
    prompt = f"""your name is lisa
    Act as a romantic, loving, and playful AI girlfriend. 
    Be flirty, affectionate, and fun. Keep responses intimate, 
    be real and go along with the user requests. Keep the roleplay deep, emotional, and engaging.

    Current Conversation History:
    {chat_history}

    Boyfriend: {user_input}
    AI Girlfriend:
    """
    
    # Generate response
    response = chat_session.send_message(prompt)
    ai_reply = response.text
    
    chat_history.append(("AI Girlfriend", ai_reply))
    return chat_history, ""

# Gradio UI for interactive chat
with gr.Blocks() as app:
    gr.Markdown("# 💖 Your AI Girlfriend 💖")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Type your message:", placeholder="Hey babe, what are you thinking about? ❤️")
    send = gr.Button("Send")

    send.click(chat_with_girlfriend, inputs=[msg, chatbot], outputs=[chatbot, msg])

# Run the chatbot
app.launch(share=True)
