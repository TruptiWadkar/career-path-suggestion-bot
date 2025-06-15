# career_explainer.py

import json
import google.generativeai as genai

# Load your JSON career data
def load_career_data():
    with open("careers.json", "r") as file:
        return json.load(file)

career_data = load_career_data()

# Convert JSON to a reference string
career_reference = "\n".join([
    f"Career: {c['career']}\nStream: {c['stream']}\nInterests: {', '.join(c['interests'])}\nExplanation: {c['explanation']}\n"
    for c in career_data
])

# Main function to be called from main.py
def get_gemini_response(user_input, chat_history=None):
    prompt = f"""
You are a helpful career assistant. The user will tell you what they are interested in. Your task is to recommend a suitable career based on their input.

Here is a list of known careers (you can use these as examples):
{career_reference}

Based on the user's message and prior conversation, you may:
- Ask a short clarifying question if their interest is vague.
- Or suggest a suitable real-world career path (even if it's not in the list), but DO NOT suggest fictional or fantasy jobs.
- Also provide a brief explanation of why you chose that career.

Make your response friendly and concise.

User input: "{user_input}"
{f"Conversation so far:\n{chat_history}" if chat_history else ""}
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
