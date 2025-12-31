# webex-compliance-automation
Python-based automation pipeline for downloading Webex recordings, extracting attendance data, uploading to Vimeo, and generating compliance-ready URLs.
# 🎥 Webex Compliance Automation Pipeline

## Overview
This project automates the end-to-end compliance workflow for recorded Webex meetings.
It downloads meeting recordings, extracts attendance data, uploads content to Vimeo,
and generates shareable URLs for audit and compliance tracking.

## Business Problem
Manual handling of compliance recordings was time-consuming, error-prone, and difficult
to audit at scale.

## Solution
An automated Python pipeline that:
- Downloads Webex meeting recordings
- Extracts attendance data
- Uploads recordings to Vimeo
- Retrieves and stores Vimeo URLs
- Produces compliance-ready outputs with zero manual intervention

## Tech Stack
- Python
- REST APIs
- OAuth / Token-based Authentication
- Logging & Error Handling
- Vimeo API
- Webex API

## Workflow
1. Authenticate with Webex API
2. Fetch meeting metadata and recordings
3. Download recordings securely
4. Extract attendance details
5. Upload recordings to Vimeo
6. Retrieve and store video URLs for compliance

## Key Features
- Fully automated compliance workflow
- Secure API authentication
- Resumable uploads and retry logic
- Structured logging for audit trails

## Results
- Reduced manual compliance work by 90%
- Improved audit traceability
- Enabled scalable handling of meeting recordings

## Future Enhancements
- Database integration for long-term storage
- Alerting on failed uploads
- Dockerization for deployment
