import os
import openai
from config import SAMBANOVA_API_KEY, SAMBANOVA_BASE_URL

# Configure Sambanova API
openai.api_key = SAMBANOVA_API_KEY
openai.api_base = SAMBANOVA_BASE_URL

def generate_excuse(category: str, humor_level: int, custom_context: str = None) -> str:
    try:
        # Create the input prompt for the Sambanova model
        custom_context_str = f"Custom Context: {custom_context}\n" if custom_context else ""
        
        prompt = (
            f"You are a witty and creative bot that generates excuses. "
            f"Category: {category}\n"
            f"Humor Level (1=Serious, 3=Ridiculous): {humor_level}\n"
            f"{custom_context_str}"
            "Generate a short, clever, and engaging excuse:"
        )
        
        # Call Sambanova's API
        response = openai.ChatCompletion.create(
            model="Meta-Llama-3.2-3B-Instruct",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Extract the excuse from the API response
        return response.choices[0].message["content"].strip()
    except Exception as e:
        raise Exception(f"Error generating excuse: {e}")
