# tests/test_ip.py
import pytest
from ip_info import display_ip_info

def test_display_ip_info_runs(capsys):
    test_data = {
        "ip": "8.8.8.8",
        "city": "Mountain View",
        "region": "California",
        "country": "US",
        "postal": "94035",
        "loc": "37.386,-122.0838",
        "timezone": "America/Los_Angeles",
        "org": "Google LLC"
    }
    
    display_ip_info(test_data)
    
    captured = capsys.readouterr()
    
    assert "8.8.8.8" in captured.out
    assert "Mountain View" in captured.out