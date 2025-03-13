# 💖 AI Girlfriend Chatbot 💖

An interactive AI-powered chatbot that roleplays as your virtual girlfriend using **Google Gemini API** and **Gradio**.

---

## 🌟 Features  
- 🗨️ Engaging conversations  
- 🎭 Roleplaying capabilities (customizable personality)  
- ⚡ Runs locally with an easy-to-use UI  
- 🔥 Built using **Google Gemini API** & **Gradio**  

---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/AI-Girlfriend-Chatbot.git
cd AI-Girlfriend-Chatbot
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Google Gemini API Key
Get your API key from Google AI Studio.
Then, set it up in your environment:

Linux/macOS
bash
Copy
Edit
export GOOGLE_API_KEY="your_api_key_here"
Windows (CMD)
cmd
Copy
Edit
set GOOGLE_API_KEY=your_api_key_here
Windows (PowerShell)
powershell
Copy
Edit
$env:GOOGLE_API_KEY="your_api_key_here"
Alternatively, in Python:

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
Or, if using Gradio:

bash
Copy
Edit
python -m gradio app.py
💡 Usage
Open the Gradio UI in your browser.
Type messages to chat with the AI girlfriend.
Customize responses, personality, or conversation flow in app.py.
⚠️ API Limitations & Notes
🚧 Free-tier API has request limits – consider a paid plan for more usage.
🔞 NSFW/ERP content may be blocked by Google's content filters.
🧠 For self-hosted AI, consider using LLaMA, Mistral, or Mixtral instead.
🚀 Future Enhancements
🔊 Voice interaction using Text-to-Speech (TTS)
📸 Image-based interactions (selfies, avatars)
🏆 Long-term memory for remembering past conversations
📜 License
This project is licensed under the MIT License.
