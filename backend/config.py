import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sambanova API configuration
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")
SAMBANOVA_BASE_URL = "https://api.sambanova.ai/v1"
