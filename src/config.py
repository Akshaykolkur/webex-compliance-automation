"""
Centralized configuration for the Webex Compliance Automation.

This module loads environment variables and exposes them
to the rest of the application.

NOTE:
This repository uses SAFE DEFAULTS to allow CI execution
and local testing without real credentials.
"""

import os
from dotenv import load_dotenv

# Load variables from .env file (if present)
load_dotenv()

# -------------------------------------------------
# Webex configuration (mock-safe)
# -------------------------------------------------
WEBEX_ACCESS_TOKEN = os.getenv(
    "WEBEX_ACCESS_TOKEN",
    "mock-webex-access-token"
)

# -------------------------------------------------
# Vimeo configuration (mock-safe)
# -------------------------------------------------
VIMEO_ACCESS_TOKEN = os.getenv(
    "VIMEO_ACCESS_TOKEN",
    "mock-vimeo-access-token"
)
VIMEO_CLIENT_ID = os.getenv(
    "VIMEO_CLIENT_ID",
    "mock-vimeo-client-id"
)
VIMEO_CLIENT_SECRET = os.getenv(
    "VIMEO_CLIENT_SECRET",
    "mock-vimeo-client-secret"
)
VIMEO_FOLDER_URI = os.getenv(
    "VIMEO_FOLDER_URI",
    "/mock/folder"
)

# -------------------------------------------------
# Google Sheets configuration (mock-safe)
# -------------------------------------------------
GOOGLE_SHEET_NAME = os.getenv(
    "GOOGLE_SHEET_NAME",
    "Mock Compliance Sheet"
)
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_FILE",
    "mock-service-account.json"
)

# -------------------------------------------------
# Environment indicator
# -------------------------------------------------
ENVIRONMENT = os.getenv("ENVIRONMENT", "mock")

