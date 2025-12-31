"""
Mock Vimeo responses.
"""

def mock_upload(file_path, title):
    return f"https://vimeo.com/mock/{title.replace(' ', '_')}"
