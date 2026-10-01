import google.generativeai as genai
import os
import json


# Gemini API key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Gemini Flash model
model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_outline(prompt):

    instruction = f"""
Create a 5-panel comic outline for this story:

{prompt}

Return JSON in this format:

[
    {{
        "panel": 1,
        "title": "Panel title",
        "scene_description": "Scene description",
        "image_prompt": "Detailed image generation prompt"
    }},
    {{
        "panel": 2,
        "title": "Panel title",
        "scene_description": "Scene description",
        "image_prompt": "Detailed image generation prompt"
    }},
    {{
        "panel": 3,
        "title": "Panel title",
        "scene_description": "Scene description",
        "image_prompt": "Detailed image generation prompt"
    }},
    {{
        "panel": 4,
        "title": "Panel title",
        "scene_description": "Scene description",
        "image_prompt": "Detailed image generation prompt"
    }},
    {{
        "panel": 5,
        "title": "Panel title",
        "scene_description": "Scene description",
        "image_prompt": "Detailed image generation prompt"
    }}
]
"""

    response = model.generate_content(
        instruction
    )

    return json.loads(response.text)