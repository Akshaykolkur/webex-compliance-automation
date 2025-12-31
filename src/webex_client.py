"""
Webex API client abstraction (mock implementation).

This module provides a sanitized, non-production interface for interacting with
Webex meeting and recording data. All responses are simulated for local testing
and demonstration purposes.
"""


class WebexClient:
    def __init__(self, access_token: str):
        """
        Initialize Webex client.

        The access token is accepted to preserve the real interface,
        but is not used in the mock implementation.
        """
        self.access_token = access_token

    def get_meeting_details(self, meeting_number, date, host_email):
        """
        Fetch mock meeting metadata.

        Returns a dictionary representing meeting information.
        """
        return {
            "meeting_number": meeting_number,
            "title": "Mock Compliance Training Session",
            "host_email": host_email,
            "date": date
        }

    def list_recordings(self, meeting_title, date, host_email, min_duration=15):
        """
        Return a list of mock recordings filtered by minimum duration.
        """
        return [
            {
                "recording_id": "mock_rec_001",
                "topic": meeting_title,
                "duration_minutes": 60
            }
        ]

    def download_recording(self, recording_id, destination_path):
        """
        Simulate downloading a recording.

        Returns a fake file path for the downloaded recording.
        """
        fake_file_path = f"{destination_path}/{recording_id}.mp4"
        print(f"[MOCK] Downloaded recording to {fake_file_path}")
        return fake_file_path
