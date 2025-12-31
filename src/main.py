"""
Entry point for Webex Compliance Automation.

This file wires together all services and starts the pipeline.
Business logic is intentionally kept out of this file.
"""

from config import WEBEX_ACCESS_TOKEN
from webex_client import WebexClient
from vimeo_client import VimeoUploader
from attendance_service import AttendanceService
from sheets_service import SheetsService
from pipeline import CompliancePipeline


def main():
    print("\nStarting Webex Compliance Automation...\n")

    # Initialize services
    webex_client = WebexClient(WEBEX_ACCESS_TOKEN)
    vimeo_uploader = VimeoUploader()
    attendance_service = AttendanceService()
    sheets_service = SheetsService()

    # Create and run pipeline
    pipeline = CompliancePipeline(
        webex=webex_client,
        vimeo=vimeo_uploader,
        attendance=attendance_service,
        sheets=sheets_service
    )

    pipeline.run()

    print("\nAutomation run completed.\n")


if __name__ == "__main__":
    main()

