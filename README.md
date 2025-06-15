# Career Path Suggestion Bot 🎓

A conversational AI assistant that suggests career paths based on user input using Gemini API and Streamlit.

## 🔧 Features

- Extracts career interests from conversation
- Maps them to known career paths (STEM, Arts, Sports, etc.)
- Generates career explanations
- Asks clarifying questions if input is vague
- Built with Gemini API + Streamlit

## 📂 Files

- `main.py` – Streamlit app interface
- `career_explainer.py` – Core logic and Gemini prompt handling
- `careers.json` – Reference data for careers

## 🚀 How to Run

1. Install dependencies:

```bash
pip install streamlit google-generativeai python-dotenv

