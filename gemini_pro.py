import google.generativeai as genai
import os


# Gemini API key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Gemini Pro model
model = genai.GenerativeModel(
    "gemini-1.5-pro"
)


def generate_story(outline):

    prompt = f"""
Create a complete comic story from the following
5-panel outline:

{outline}

For every panel provide:

- Caption
- Narration
- Character dialogue

Make the story consistent across all five panels.
"""

    response = model.generate_content(
        prompt
    )

    return response.text