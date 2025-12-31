"""
Google Sheets service abstraction (mock implementation).

This module simulates reading from and writing to Google Sheets
for local testing and demonstration purposes.
"""


class SheetsService:
    def __init__(self):
        """
        Initialize mock Google Sheets service.

        Real authentication and API calls are intentionally omitted.
        """
        pass

    def get_pending_batches(self):
        """
        Simulate retrieving pending batch records.

        Returns a list of mock batch configurations.
        """
        print("[MOCK] Fetching pending batches from Google Sheets")

        return [
            {
                "meeting_number": "123456789",
                "date": "2025-01-15",
                "host_email": "host@example.com"
            }
        ]

    def update_status(self, batch, vimeo_url=None, attendance_path=None):
        """
        Simulate updating processing status in Google Sheets.
        """
        print(
            f"[MOCK] Updated status for meeting {batch['meeting_number']}"
        )

        if vimeo_url:
            print(f"[MOCK] Vimeo URL saved: {vimeo_url}")

        if attendance_path:
            print(f"[MOCK] Attendance file saved: {attendance_path}")
