import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# headers = {
#     "Authorization": f"Bearer {OPENAI_API_KEY}",
#     "Content-Type": "application/json"
# }
openai.api_key = OPENAI_API_KEY


def summarise_text(text):
    """
    Use the OpenAI API to get a summarized version of the provided text.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The summarized text.
    """

    response = openai.ChatCompletion.create(model="gpt-4",
                                            messages=[
                                                {
                                                    "role": "user", "content": f"Summarize the following email(s) in English: {text}"
                                                }
                                            ])

    if "choices" in response and len(response["choices"]) > 0:
        return response["choices"][0]["message"]["content"].strip()
    else:
        return "Summary not available."


if __name__ == '__main__':
    # Example usage:
    summary = summarise_text("Hello, just checking in to see how things are...")
    print(summary)
