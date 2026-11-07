
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("GEMINI_API_KEY is missing. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a message to Gemini
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="In two sentences, explain what a virtual environment is."
)

# Print the answer
print(response.text)