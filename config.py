import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Dhan API credentials
CLIENT_ID = os.getenv('CLIENT_ID')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

# Strategy-related constants
TIME_OF_EXECUTION = "9:25"  # Example execution time
TOP_N_SCRIPTS = 1  # Number of top gainers/losers to trade


### Run this when the scrip runs rather than at a certain time
