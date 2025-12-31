# 🎥 Webex Compliance Automation Pipeline

Python-based automation pipeline for downloading Webex recordings, extracting
attendance data, uploading videos to Vimeo, and generating compliance-ready URLs.

---

## Overview
This project showcases a production-style automation pipeline designed to
process Webex meeting recordings for compliance and audit purposes.

The system automates:
- Retrieval of meeting metadata
- Download and processing of recordings
- Upload of recordings to Vimeo
- Extraction of attendance reports
- Centralized tracking via Google Sheets

This repository contains a **sanitized and modularized** version of the system,
focused on architecture, orchestration, and automation design.

---

## Problem Statement
Manual handling of Webex compliance recordings is time-consuming, error-prone,
and difficult to scale across large volumes of meetings.

---

## Solution Overview
A modular automation pipeline that separates concerns across:
- API clients
- Orchestration logic
- External service integrations
- Configuration management

This design improves scalability, maintainability, and secure handling of
sensitive credentials.

---

## Architecture

```text
src/
├── main.py               # Application entry point
├── config.py             # Centralized configuration
├── pipeline.py           # Automation orchestration
├── webex_client.py       # Webex API abstraction
├── vimeo_client.py       # Vimeo upload abstraction
├── attendance_service.py # Attendance handling
└── sheets_service.py     # Google Sheets integration

```

## High-Level Workflow
1. Load configuration from environment variables
2. Retrieve pending batch records
3. Fetch meeting and recording metadata from Webex
4. Download and upload recordings to Vimeo
5. Retrieve attendance reports
6. Update tracking and audit records

---

## Design Principles
- Separation of concerns
- Secure handling of credentials
- Modular and testable architecture
- Production-oriented automation design

---

## Notes on Code Samples
This repository intentionally excludes:
- Production credentials and secrets
- Company-specific workflows
- Full API implementations

The focus is on **system design and automation architecture**, not exposing
sensitive operational logic.

---

## Tech Stack
- Python
- REST APIs
- Automation orchestration
- Environment-based configuration
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
