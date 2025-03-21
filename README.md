# 🤖 Greeting Agent

## 📌 Overview

This is a simple AI-powered Greeting Agent that responds to user inputs based on predefined rules. It uses OpenAI's API (incorrectly referenced as Gemini in the code) to generate responses.

## ✨ Features

- ✅ Responds with **"Salam from Bisma Yousuf"** when the user says **"hi"**.
- ✅ Responds with **"Allah Hafiz from Bisma Yousuf"** when the user says **"bye"**.
- ✅ Responds with **"Bisma Yousuf is here just for greeting, nothing else sorry."** for any other input.

## 🔧 Requirements

- 🐍 Python 3.8+
- 📦 `dotenv` for environment variable management
- 🔑 A compatible AI API key (OpenAI/Gemini)

## 🚀 Installation

1. 📥 Clone the repository:
   ```sh
   git clone https://github.com/yourusername/greeting-agent.git
   cd greeting-agent
   ```
2. 📦 Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. 📝 Create a `.env` file and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## ▶️ Usage

Run the script:

```sh
python greeting_agent.py
```

🗣️ Enter a greeting, and the agent will respond accordingly.

## ⚠️ Issues

- 🔍 Ensure the API key is correct and valid.
- ❗ The AI provider setup may not work correctly with Gemini.
- 🛠️ The `Runner.run_sync` function should be verified with your AI framework.

