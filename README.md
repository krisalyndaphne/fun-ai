💖 AI Girlfriend Chatbot 💖
An interactive AI-powered chatbot that roleplays as your virtual girlfriend using Google Gemini API and Gradio.

🌟 Features
✅ Engaging conversations with AI
✅ Roleplaying capabilities (customizable personality)
✅ Built using Google Gemini API & Gradio
✅ Runs locally with an easy-to-use UI

🛠 Installation & Setup
1️⃣ Clone the Repository
    git clone https://github.com/yourusername/AI-Girlfriend-Chatbot.git
    cd AI-Girlfriend-Chatbot
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Google Gemini API Key
Get your API key from Google AI Studio
Create a .env file or set it in your environment:
bash
Copy
Edit
export GOOGLE_API_KEY="your_api_key_here"
Or in Python:

python
Copy
Edit
import os
os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
4️⃣ Run the Chatbot
bash
Copy
Edit
python app.py
or if using Gradio:

bash
Copy
Edit
python -m gradio app.py
💡 Usage
1️⃣ Open the Gradio UI in your browser.
2️⃣ Type messages to chat with the AI girlfriend.
3️⃣ Customize responses, personality, or conversation flow in app.py.

⚠️ API Limitations & Notes
Free-tier API has request limits – consider a paid plan for more usage.
NSFW/ERP content may be blocked by Google's content filters.
For self-hosted AI, consider using LLaMA, Mistral, or Mixtral instead.
🚀 Future Enhancements
✅ Voice interaction using Text-to-Speech (TTS)
✅ Image-based interactions (sending selfies, generating avatars)
✅ Long-term memory for remembering past conversations

📜 License
This project is licensed under the MIT License.

Let me know if you need any tweaks or extra features! 🚀🔥

