"""
Automation pipeline orchestration (runnable mock).

This module coordinates the full automation flow using
mock service implementations. It demonstrates how the
system operates end-to-end without real external APIs.
"""


class CompliancePipeline:
    def __init__(self, webex, vimeo, attendance, sheets):
        """
        Initialize the pipeline with required services.
        """
        self.webex = webex
        self.vimeo = vimeo
        self.attendance = attendance
        self.sheets = sheets

    def run(self):
        """
        Execute the automation pipeline using mock services.
        """
        print("\n=== Starting Compliance Automation Pipeline ===\n")

        batches = self.sheets.get_pending_batches()

        if not batches:
            print("[PIPELINE] No pending batches found")
            return

        for batch in batches:
            print(
                f"\n[PIPELINE] Processing meeting "
                f"{batch['meeting_number']} ({batch['date']})"
            )

            # Step 1: Get meeting details
            meeting = self.webex.get_meeting_details(
                batch["meeting_number"],
                batch["date"],
                batch["host_email"]
            )

            # Step 2: List recordings
            recordings = self.webex.list_recordings(
                meeting["title"],
                batch["date"],
                batch["host_email"]
            )

            for recording in recordings:
                # Step 3: Download recording
                file_path = self.webex.download_recording(
                    recording["recording_id"],
                    destination_path="downloads"
                )

                # Step 4: Upload to Vimeo
                vimeo_url = self.vimeo.upload(
                    file_path=file_path,
                    title=meeting["title"]
                )

                # Step 5: Download attendance report
                attendance_path = self.attendance.download(
                    meeting_number=batch["meeting_number"],
                    recording_id=recording["recording_id"]
                )

                # Step 6: Update tracking sheet
                self.sheets.update_status(
                    batch=batch,
                    vimeo_url=vimeo_url,
                    attendance_path=attendance_path
                )

        print("\n=== Compliance Automation Pipeline Completed ===\n")
