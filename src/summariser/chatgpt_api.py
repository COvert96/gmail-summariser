import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_ENDPOINT = "https://api.openai.com/v1/engines/davinci-completion/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}


def summarise_text(text):
    """
    Use the OpenAI API to get a summarized version of the provided text.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """
    payload = {
        "prompt": f"Summarize the following email: {text}",
        "max_tokens": 150  # You can adjust this based on desired summary length.
    }

    response = requests.post(OPENAI_API_ENDPOINT, headers=headers, data=json.dumps(payload))
    response_json = response.json()

    if "choices" in response_json and len(response_json["choices"]) > 0:
        return response_json["choices"][0]["text"].strip()
    else:
        return "Summary not available."


if __name__ == '__main__':
    # Example usage:
    summary = summarize_text("Hello, just checking in to see how things are...")
    print(summary)
