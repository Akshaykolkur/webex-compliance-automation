"""
Vimeo upload client abstraction (mock implementation).

This module simulates video uploads to Vimeo for local testing
and demonstration purposes.
"""


class VimeoUploader:
    def __init__(self):
        """
        Initialize Vimeo uploader.

        Real authentication and SDK configuration are intentionally omitted.
        """
        pass

    def upload(self, file_path, title, description=""):
        """
        Simulate uploading a video to Vimeo.

        Returns a mock public Vimeo URL.
        """
        safe_title = title.replace(" ", "_").lower()
        mock_url = f"https://vimeo.com/mock/{safe_title}"

        print(f"[MOCK] Uploaded '{file_path}' to Vimeo")
        print(f"[MOCK] Vimeo URL: {mock_url}")

        return mock_url
