"""
Attendance report handling service (mock implementation).

This module simulates downloading attendance reports for
local testing and demonstration purposes.
"""


class AttendanceService:
    def __init__(self):
        """
        Initialize attendance service.

        Real API calls and file downloads are intentionally omitted.
        """
        pass

    def download(self, meeting_number, recording_id):
        """
        Simulate downloading an attendance report.

        Returns a fake file path to the attendance report.
        """
        fake_path = f"attendance_reports/{meeting_number}.csv"
        print(
            f"[MOCK] Downloaded attendance report for "
            f"meeting {meeting_number} (recording {recording_id})"
        )
        print(f"[MOCK] Attendance file path: {fake_path}")

        return fake_path
