"""
Centralized configuration for the Webex Compliance Automation.

This module loads environment variables and exposes them
to the rest of the application.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file (if present)
load_dotenv()

# Webex configuration
WEBEX_ACCESS_TOKEN = os.getenv("WEBEX_ACCESS_TOKEN")

# Vimeo configuration
VIMEO_ACCESS_TOKEN = os.getenv("VIMEO_ACCESS_TOKEN")
VIMEO_CLIENT_ID = os.getenv("VIMEO_CLIENT_ID")
VIMEO_CLIENT_SECRET = os.getenv("VIMEO_CLIENT_SECRET")
VIMEO_FOLDER_URI = os.getenv("VIMEO_FOLDER_URI")

# Google Sheets configuration
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Webex Recordings")
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_FILE",
    "service_account.json"
)

# Basic validation (fail fast)
if not WEBEX_ACCESS_TOKEN:
    raise ValueError("WEBEX_ACCESS_TOKEN is not set")

if not VIMEO_ACCESS_TOKEN:
    raise ValueError("VIMEO_ACCESS_TOKEN is not set")
